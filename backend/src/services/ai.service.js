const natural = require("natural"); // Optional for keyword extraction
const { calculateMetrics } = require("./metrics.service");

exports.processQuery = async (query) => {
  const keywords = query.toLowerCase().split(/\s+/);

  if (keywords.includes("total") && keywords.includes("sales")) {
    // Dummy data or fetch from your DB/Baserow
    const dummySales = [
      { product: "Apple", amount: 120 },
      { product: "Banana", amount: 80 },
    ];
    const metrics = calculateMetrics(dummySales);
    return { type: "metric", label: "Total Sales", data: metrics.totalSales };
  }

  return {
    type: "text",
    response: `Sorry, I couldn't understand the query: "${query}"`,
  };
};
