const express = require('express');
const router = express.Router();

const { timeout } = require('../config.json');

router.get('/status', (req, res) => {
   setTimeout(() => {
       res.json({ status: 'ok', timeout });
   }, 100);
});

module.exports = router;
