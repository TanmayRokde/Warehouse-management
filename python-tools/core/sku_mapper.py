import pandas as pd
from .loader import load_mapping
from .mapping_utils import is_combo_product, split_combo_skus, validate_sku_format
from .logger import log_info, log_warning

class SKUMappingTool:
    def __init__(self):
        self.mapping_df = load_mapping()

    def get_msku(self, sku):
        if is_combo_product(sku):
            parts = split_combo_skus(sku)
            mapped = [self._get_single_mapping(p) for p in parts]
            return "+".join(mapped)
        return self._get_single_mapping(sku)

    def _get_single_mapping(self, sku):
        sku = sku.strip()
        if not validate_sku_format(sku):
            log_warning(f"Invalid SKU format: {sku}")
            return "INVALID_SKU"

        row = self.mapping_df[self.mapping_df["SKU"] == sku]
        if not row.empty:
            return row.iloc[0]["MSKU"]
        else:
            log_warning(f"Mapping not found for SKU: {sku}")
            return "UNMAPPED"

    def map_sales_data(self, sales_df):
        sales_df["MSKU"] = sales_df["SKU"].apply(self.get_msku)
        return sales_df
