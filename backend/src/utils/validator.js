exports.isValidSKU = (sku) => {
  return typeof sku === 'string' && sku.trim().length > 0;
};
