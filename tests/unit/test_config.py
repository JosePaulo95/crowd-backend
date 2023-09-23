import unittest
from app.repositories.config import contexts_config


class TestConfig(unittest.TestCase):
    def test_contexts_config(self):
        contexts = contexts_config()
        self.assertIsInstance(contexts, dict)
        self.assertIn("youtube", contexts)
        # mais asserções baseadas em suas especificações


if __name__ == "__main__":
    unittest.main()
