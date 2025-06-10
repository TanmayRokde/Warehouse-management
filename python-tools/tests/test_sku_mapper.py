import unittest
import pandas as pd
from core.sku_mapper import SKUMappingTool

class TestSKUMapping(unittest.TestCase):
    def setUp(self):
        self.tool = SKUMappingTool()

    def test_single_sku(self):
        self.assertEqual(self.tool.get_msku("GLD"), "Golden Apple")

    def test_unmapped_sku(self):
        self.assertEqual(self.tool.get_msku("XYZ"), "UNMAPPED")

    def test_combo_sku(self):
        self.assertEqual(self.tool.get_msku("GLD+GRN"), "Golden Apple+Green Apple")
