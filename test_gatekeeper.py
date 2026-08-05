import unittest
from unittest.mock import MagicMock
from app.gatekeeper import Gatekeeper

class TestGatekeeper(unittest.TestCase):
    def setUp(self):
        self.alice = Gatekeeper()
        self.alice.manage_connectors("google_drive", "dummy_token")
        self.db = MagicMock()

    def test_spawn_subworker(self):
        worker = self.alice.spawn_subworker("TestWorker", "TestTask", self.db)
        self.assertEqual(worker.name, "TestWorker")
        self.assertEqual(worker.status, "Running")
        self.assertEqual(worker.task, "TestTask")
        self.db.add.assert_called_once()
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once_with(worker)

    def test_search_google_drive(self):
        results = self.alice.search_google_drive("3D glasses")
        self.assertTrue(isinstance(results, list))
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["file"], "3D_Glasses_Blueprints.pdf")

    def test_ingest_chat(self):
        log = self.alice.ingest_ai_chat("OpenAI", {"model": "gpt-4"}, "Hello Alice", self.db)
        self.assertEqual(log.ai_source, "OpenAI")
        self.assertEqual(log.content, "Hello Alice")
        self.db.add.assert_called_once()
        self.db.commit.assert_called_once()
        self.db.refresh.assert_called_once_with(log)


    def test_generate_audio(self):
        mock_query = MagicMock()
        self.db.query.return_value = mock_query
        mock_filter1 = MagicMock()
        mock_query.filter.return_value = mock_filter1
        mock_filter2 = MagicMock()
        mock_filter1.filter.return_value = mock_filter2

        mock_chat = MagicMock()
        mock_chat.id = 1
        mock_chat.ai_source = "ChatGPT"
        mock_chat.audio_file_path = None
        mock_filter2.all.return_value = [mock_chat]

        processed = self.alice.generate_audio_for_chats(["ChatGPT"], self.db)

        self.assertEqual(len(processed), 1)
        self.assertEqual(processed[0], 1)
        self.assertEqual(mock_chat.audio_file_path, "/static/audio/alice_whisper_fr_1.mp3")
        self.db.commit.assert_called()

if __name__ == '__main__':
    unittest.main()
