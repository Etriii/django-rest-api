# Django School Management API

A **Django + Django REST Framework (DRF)** project for managing schools, institutes, programs, students, and users.  
Includes role-based permissions, schema-based API docs, and a custom user model with status and access control.

---

## 🚀 Features

- **Custom User Model** with roles (superuser, staff, etc.) and status (active, inactive, suspended).
- **School / Institute / Program Models** with relationships:
  - A **School** can have many Institutes.
  - An **Institute** can have many Programs.
- **Dynamic Serializers** per action (create, update, read, delete).
- **Role & Scope Permissions**:
  - Superadmins → full access.
  - Scoped by School / Institute where applicable.
- **Interactive API Docs** (Swagger / ReDoc).
- **Admin Panel** for easy management.

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
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

