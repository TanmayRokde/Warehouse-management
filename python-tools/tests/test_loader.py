import unittest
from core.loader import load_mapping

class TestLoader(unittest.TestCase):
    def test_load_mapping(self):
        df = load_mapping()
        self.assertIn("SKU", df.columns)
        self.assertIn("MSKU", df.columns)
