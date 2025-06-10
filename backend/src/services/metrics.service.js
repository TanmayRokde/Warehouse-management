exports.calculateMetrics = (salesData) => {
  const totalSales = salesData.reduce((sum, item) => sum + Number(item.amount || 0), 0);
  return { totalSales };
};
