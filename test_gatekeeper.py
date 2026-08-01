import unittest
from app.gatekeeper import Gatekeeper

class TestGatekeeper(unittest.TestCase):
    def setUp(self):
        self.alice = Gatekeeper()
        self.alice.manage_connectors("google_drive", "dummy_token")

    def test_spawn_subworker(self):
        worker = self.alice.spawn_subworker("TestWorker", "TestTask")
        self.assertEqual(worker.name, "TestWorker")
        self.assertEqual(worker.status, "Running")
        self.assertEqual(worker.task, "TestTask")
        self.assertEqual(len(self.alice.subworkers), 1)

    def test_search_google_drive(self):
        results = self.alice.search_google_drive("3D glasses")
        self.assertTrue(isinstance(results, list))
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["file"], "3D_Glasses_Blueprints.pdf")

    def test_ingest_chat(self):
        log = self.alice.ingest_ai_chat("OpenAI", {"model": "gpt-4"}, "Hello Alice")
        self.assertEqual(log.ai_source, "OpenAI")
        self.assertEqual(log.content, "Hello Alice")

if __name__ == '__main__':
    unittest.main()
