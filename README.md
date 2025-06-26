# 📝 Task Management Tool (Django)

A simple web-based **Task Management Application** built using **Python Django**, allowing users to create, view, update, and delete tasks. This app is deployed live using **Render**.

---

## 🌐 Live Demo

👉 [Visit the Live App](https://task-management-tool-4bzh.onrender.com)

---

## 🚀 Features

- Create new tasks with title and description
- Mark tasks as completed or not
- Update existing tasks
- Delete tasks
- Responsive and clean interface

---

## 🛠️ Tech Stack

| Layer      | Tech Used            |
|------------|----------------------|
| Language   | Python 3.10          |
| Framework  | Django 5.2.3         |
| Database   | SQLite (Django default) |
| Deployment | Render               |
| Server     | Gunicorn             |
| Frontend   | HTML, CSS            |

---

## 🗂️ Project Structure

```
taskflow_django/
├── manage.py
├── render.yaml
├── requirements.txt
├── taskflow_django/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tasks/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
├── templates/
│   ├── base.html
│   └── tasks/
│       ├── task_list.html
│       └── task_form.html
├── static/
│   └── css/
│       └── style.css
```

---

## ⚙️ Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Thesushmit/Task-Management-Tool.git
cd Task-Management-Tool
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the Development Server
```bash
python manage.py runserver
```

Then visit: `http://127.0.0.1:8000`

---

## ☁️ Deployment on Render

This project includes a `render.yaml` file for automatic deployment. Here's how it's deployed:

- Render detects `render.yaml`
- Uses `gunicorn` to serve the Django app
- No database setup required for SQLite (default)

You can view the deployment here:  
🌍 [https://task-management-tool-4bzh.onrender.com](https://task-management-tool-4bzh.onrender.com)

---

## 🙌 Acknowledgements

This project was developed by **Sushmit Partakke** as part of a software capstone internship project.

---

