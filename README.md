# Django Blog Application 📝

A fully featured blog platform built with **Django**, supporting user authentication, CRUD operations for posts, pagination, and group-based permissions. This project demonstrates modern Django practices, containerization with Docker, and CI/CD automation using GitHub Actions.

---

## 🚀 Features
- User registration, login, logout, and password reset
- Create, edit, delete blog posts
- Rich text content with categories and tags
- Pagination for post listings
- Group & permission management (e.g., Registered User, Admin)
- Responsive UI with Bootstrap
- Error handling pages (404, 500)
- Dockerized for easy deployment
- CI/CD pipeline with GitHub Actions

---

## 📂 Project Structure



---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/django-blog-app.git
cd django-blog-app


### 2.Create and activate virtual environment

python -m venv Blog_env
# Windows
Blog_env\Scripts\activate
# Linux/Mac
source Blog_env/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

docker build -t django-blog .
docker run -p 8000:8000 django-blog

docker-compose up --build

🔄 CI/CD with GitHub Actions
This project includes a GitHub Actions workflow (.github/workflows/deploy.yml) that:
- Builds Docker image on every push
- Runs tests
- Pushes image to DockerHub/GitHub Container Registry
- Deploys to host (Render/Heroku/Railway)

🌐 Deployment (Free Hosting Options)
- Render: Simple Docker deploy with free tier
- Railway: GitHub integration, free tier
- PythonAnywhere: Free tier (without Docker)
- Heroku: Limited free tier

python manage.py test


---

This README is **production-ready**: it explains setup, Dockerization, CI/CD, deployment, and contribution guidelines.  

👉 I can also tailor this README with **badges** (build status, Docker pulls, license, etc.) if you’d like a more professional GitHub look. Would you like me to add those badges at the top?
