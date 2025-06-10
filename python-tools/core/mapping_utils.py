def validate_sku_format(sku: str) -> bool:
    return isinstance(sku, str) and len(sku.strip()) > 0

def is_combo_product(sku: str) -> bool:
    return "+" in sku

def split_combo_skus(combo_sku: str):
    return [s.strip() for s in combo_sku.split("+")]
