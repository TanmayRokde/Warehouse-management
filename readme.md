# 📦 Warehouse Management System (WMS)

A modular, full-stack warehouse management system for SKU/MSKU mapping, data cleaning, querying, and visualization.

---

## 🗂 Folder Structure

```
Warehouse-management/
├── python-tools/         # Python GUI for SKU to MSKU mapping
├── backend/              # Node.js backend API with AI, Baserow integration
├── frontend/             # React frontend for uploading, querying, charting
├── docker-compose.yml    # Docker orchestration file
├── README.md
```

---

## 🧹 python-tools

### Description
A standalone Tkinter-based GUI tool to:
- Map SKUs → MSKUs interactively
- Import/export CSV files
- Log unmapped SKUs

### Tech Stack
- Python 3.10+
- `tkinter`, `pandas`, `csv`, `os`

### Run Locally
```bash
cd python-tools
pip install -r requirements.txt
python run.py
```

---

## ⚙️ backend

### Description
Handles:
- CSV uploads
- SKU/MSKU mapping
- AI-driven queries
- Integration with Baserow or NoCodeDB

### Tech Stack
- Node.js + Express
- Multer, Axios, csv-parser
- Optional: Prisma (PostgreSQL), dotenv

### Run Locally
```bash
cd backend
npm install
npm run dev
```

### Docker
```bash
docker build -t wms-backend ./backend
docker run -p 3000:3000 wms-backend
```

---

## 💻 frontend

### Description
React-based UI to:
- Upload sales data
- Explore mapping
- Submit natural language queries
- View generated charts and metrics

### Tech Stack
- React + Vite
- TailwindCSS
- Axios, Chart.js/Recharts

### Run Locally
```bash
cd frontend
npm install
npm run dev
```

### Docker
```bash
docker build -t wms-frontend ./frontend
docker run -p 5173:5173 wms-frontend
```

---

## 🐳 Docker Compose (Monorepo)

### `docker-compose.yml`
```yaml
version: "3.8"
services:
  backend:
    build: ./backend
    ports:
      - "3000:3000"
    volumes:
      - ./backend:/app
    environment:
      - NODE_ENV=development

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    depends_on:
      - backend
    volumes:
      - ./frontend:/app
```

### Run Entire Stack
```bash
docker-compose up --build
```

---

## 📁 Environment Variables

### `backend/src/config/env.js`
```js
module.exports = {
  BASEROW_API_KEY: process.env.BASEROW_API_KEY,
  DB_URL: process.env.DB_URL,
};
```

Create a `.env` file in the backend root:

```
BASEROW_API_KEY=your_baserow_api_key
DB_URL=your_database_url
```

---

## ✅ Features

| Module         | Functionality                                 |
|----------------|-----------------------------------------------|
| Python GUI     | Manual SKU ⇄ MSKU mapping                     |
| Node.js API    | Upload, remap, metrics, AI/NL query support   |
| React Frontend | Data upload, dashboard, querying, charts      |
| Docker         | Unified environment across frontend/backend   |

---

## 🧪 Testing

### Backend
```bash
npm run test
```

Basic test coverage for mapping routes and logic.

---

## 🔮 Roadmap

- [ ] Persistent mapping storage (Postgres or Baserow)
- [ ] AI query → SQL → visualization
- [ ] Editable frontend tables and logs
- [ ] Multi-user role-based UI

---

## 👨‍💻 Author

Built by [Tanmay Rokde](https://github.com/TanmayRokde) – IITian, backend engineer, and full-stack enthusiast.

---

## 🪪 License

MIT © 2025
