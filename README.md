## 📦 Installation

### 1. Clone the Repository
```bash
git https://github.com/Etriii/dnsc_systems_api.git
cd dnsc_systems_api
```

### 2. Create Virtual Environment (Optional but preffered: allows you to manage project-specific dependencies without interfering with other projects or the original Python installation)
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the server
```bash
python manage.py runserver
```

### Access URLS
```bash
Once the server is running at http://127.0.0.1:8000/, you can access:

Django Admin → http://127.0.0.1:8000/admin/

API Root → http://127.0.0.1:8000/api/v1/

Swagger: http://127.0.0.1:8000/api/docs/swagger/
Redoc: http://127.0.0.1:8000/api/docs/redoc/

Raw OpenAPI Schema (JSON) → http://127.0.0.1:8000/api/schema/
```

