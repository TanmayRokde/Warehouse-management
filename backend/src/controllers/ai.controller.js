const aiService = require('../services/ai.service');

exports.queryData = async (req, res) => {
  try {
    const { query } = req.body;
    const result = await aiService.processQuery(query);
    res.json({ success: true, result });
  } catch (err) {
    res.status(500).json({ success: false, error: err.message });
  }
};
