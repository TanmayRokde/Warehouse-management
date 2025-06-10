const axios = require('axios');
const { BASEROW_API_KEY } = require('../config/env');

exports.pushToBaserow = async (data) => {
  return axios.post('https://api.baserow.io/api/database/rows/table/1/', data, {
    headers: { Authorization: `Token ${BASEROW_API_KEY}` }
  });
};
