# Django-BigBuy-API

# 🛒 BigBuy - Django eCommerce API

## Overview
BigBuy is a Django-based eCommerce API that allows users to manage products, categories, orders, and authentication. It uses **Django Rest Framework (DRF)** for API development and **Swagger UI** for API documentation.

## Features
✅ User authentication (JWT-based login & registration)  
✅ Product management (CRUD operations)  
✅ Order processing  
✅ Category-based product listing  
✅ Swagger API documentation  

## 🚀 Technologies Used
- 🐍 Python (Django, Django Rest Framework)
- 🗄️ PostgreSQL/MySQL (Database)
- 🔐 JWT Authentication
- 📄 Swagger UI (API Documentation)
- 🐳 Docker (Optional for containerization)

## 📥 Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)
- Virtualenv (recommended for dependency isolation)
- PostgreSQL/MySQL (or SQLite for development)

### Steps to Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Manikandan-2205/BigBuy.git
   cd BigBuy
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (Create `.env` file in the root directory)
   ```ini
   SECRET_KEY="Key"
   DEBUG=True
   DATABASE_URL=DbLink
   ```

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 📜 API Documentation with Swagger
BigBuy uses `drf-yasg` to generate API documentation.

1. Install `drf-yasg` if not installed:
   ```bash
   pip install drf-yasg
   ```

2. Check the API documentation at:
   - 📌 Swagger UI: `http://127.0.0.1:8000/apidocs/` -- swaggerui-link
   - 📌 Redoc UI: `http://127.0.0.1:8000/redoc/`

## 🧪 Running Tests
To run tests, use:
```bash
python manage.py test
```

## 🚀 Deployment (Optional)
Use Docker for deployment:
```bash
docker build -t bigbuy .
docker run -p 8000:8000 bigbuy
```

## 🤝 Contributing
1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push and submit a PR

## 📜 License
This project is licensed under the MIT License.

---
### 📩 Contact
For queries, contact **manikandanp.2205@gmail.com** or create an issue in the repository.
