# 🏬 Warehouse Management System (WMS)

This repository is a modular Warehouse Management System designed to streamline SKU mapping, product data management, and analytics with AI-powered querying. It is divided into three main parts:

---

## 🧩 Structure

```
Warehouse-management/
├── python-tools/      # Python GUI tool for SKU to MSKU mapping (Data Cleaning)
├── backend/           # Node.js backend with Express and optional Prisma
└── frontend/          # React.js frontend for visualizations and interaction
```

---

## 1️⃣ Python Tools (Data Cleaning GUI)

**Folder:** `python-tools/`

### 🎯 Purpose:
- GUI-based interface for mapping **SKUs → MSKUs**
- Exporting cleaned mapping data to CSV
- Used as a pre-processing step before backend ingestion

### 🔧 Features:
- Load raw sales CSV
- Map SKUs to MSKUs (auto/manual)
- Handle combo products
- Export cleaned CSV for upload

### 📂 Structure:
```
python-tools/
├── core/           # Mapping logic, validators, loaders
├── gui/            # Tkinter-based GUI
├── data/           # Sample input/output files
├── tests/          # Unit tests
└── run.py          # Entry point to launch the app
```

### ▶️ Run it:
```bash
cd python-tools
python run.py
```

---

## 2️⃣ Backend (Node.js API)

**Folder:** `backend/`

### 🎯 Purpose:
- REST API to handle file uploads, mapping logic, and AI-based querying
- Optional Prisma + PostgreSQL integration

### 🔧 Features:
- Upload cleaned CSVs
- Re-map SKUs server-side (optional)
- Run AI-powered natural language queries (e.g. "Show total sales")
- Metrics calculation and Baserow/NoCodeDB sync

### 📂 Structure:
```
backend/
├── prisma/         # Optional Prisma DB schema
├── src/
│   ├── controllers/
│   ├── services/
│   ├── models/
│   ├── routes/
│   └── utils/
├── tests/          # Sample test files
├── package.json
└── tsconfig.json   # Present but unused
```

### ▶️ Run it:
```bash
cd backend
npm install
npm run dev
```

> 🔑 Add a `.env` file:
```env
PORT=3000
BASEROW_API_KEY=your_key_here
DATABASE_URL=postgresql://user:pass@localhost:5432/wms
```

---

## 3️⃣ Frontend (React.js)

**Folder:** `frontend/`

### 🎯 Purpose:
- Web interface to:
  - Upload mapping files
  - Visualize order/product data
  - Run natural language queries
  - Display AI-generated metrics and charts

### 📂 Structure:
```
frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   └── App.jsx, index.js, etc.
├── public/
└── package.json
```

### ▶️ Run it:
```bash
cd frontend
npm install
npm start
```

---

## 🧠 AI Integration

- **Text-to-SQL queries**: Users can ask questions like:
  - *"What were the total sales last week?"*
  - *"Show most returned products"*
- Uses keyword-matching now, can be upgraded to OpenAI/LangChain/DB-GPT

---

## 🚀 Roadmap

- [x] SKU → MSKU mapper (GUI)
- [x] File upload + backend parsing
- [x] Basic AI query handling
- [ ] Integrate full database
- [ ] Advanced charts in frontend
- [ ] Auth and role-based dashboards

---

## 🛠️ Dev Scripts

```bash
# Backend
cd backend && npm run dev

# Frontend
cd frontend && npm start

# Python GUI
cd python-tools && python run.py
```

---

## 🧪 Tests

```bash
# Run backend test cases
cd backend
npm test
```

---

## 👨‍💻 Author

Made by [@TanmayRokde](https://github.com/TanmayRokde)

---

## 📝 License

This project is MIT licensed.