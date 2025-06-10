const fileService = require('../services/file.service');
const multer = require('multer');
const upload = multer({ dest: 'uploads/' });

exports.uploadCSV = [
  upload.single('file'),
  async (req, res) => {
    try {
      const result = await fileService.parseCSV(req.file.path);
      res.json({ success: true, data: result });
    } catch (err) {
      res.status(500).json({ success: false, message: err.message });
    }
  }
];
