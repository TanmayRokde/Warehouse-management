const express = require('express');
const { remapSKUs } = require('../controllers/mapping.controller');
const router = express.Router();

router.post('/remap', remapSKUs);
module.exports = router;
