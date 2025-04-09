### 🔹 Step 1: Clone the Project

```bash
git clone https://github.com/Navin-nash/editor.git
cd backend```

### 🔹 Step 2: Run the backend FASTAPI
```cd backend
python -m venv venv
source venv/bin/activate        # or use venv\Scripts\activate on Windows
pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

### Step 3: Run the frontend
```
cd frontend
npm install

npm run dev```



