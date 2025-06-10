const express = require('express');
const { queryData } = require('../controllers/ai.controller');
const router = express.Router();

router.post('/query', queryData);
module.exports = router;
