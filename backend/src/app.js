const express = require('express');
const cors = require('cors');
const uploadRoutes = require('./routes/upload.routes');
const mappingRoutes = require('./routes/mapping.routes');
const aiRoutes = require('./routes/ai.routes');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

app.use('/api/upload', uploadRoutes);
app.use('/api/mapping', mappingRoutes);
app.use('/api/ai', aiRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
