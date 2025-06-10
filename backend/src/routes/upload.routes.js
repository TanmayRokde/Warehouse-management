const express = require('express');
const { uploadCSV } = require('../controllers/upload.controller');
const router = express.Router();

router.post('/', uploadCSV);
module.exports = router;
