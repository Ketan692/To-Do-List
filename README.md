# 📝 To-Do List (Django Project)

A simple To-Do List web application built with Django. This app allows users to register, log in, and manage their personal task lists — including adding, viewing, and completing tasks.

## 🚀 Features

- User Registration and Login
- Add, View, and Delete Tasks
- Mark Tasks as Completed
- Simple, responsive UI using Django Templates

## 🏗️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Database**: SQLite (default Django DB)
- **Authentication**: Django’s built-in user model

---

## ⚙️ Getting Started

### 🔧 Prerequisites

Make sure you have the following installed:

- Python 3.8+
- pip (Python package manager)
- virtualenv (optional but recommended)

### 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/Ketan692/To-Do-List.git
cd To-Do-List
```

2. **Create and activate a virtual environment**

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```
> If `requirements.txt` is missing, install Django manually:
```bash
pip install django
```

4. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Open the app in your browser**
```bash
http://127.0.0.1:8000/
```

## 📁 Project Structure
```
To-Do-List/
├── accounts/ # Handles user authentication
│ ├── views.py
│ ├── urls.py
│ └── ...
├── home/ # Main to-do app logic
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── ...
├── myproject/ # Django project config
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── static/ # Static files (CSS, JS)
├── templates/ # HTML templates
├── db.sqlite3 # Default SQLite database
├── manage.py # Django management script
```

## 🛡️ License
This project is open source and free to use.


## 🙋‍♂️ Author
**Ketan692**<br>
[GitHub Profile](https://github.com/Ketan692)







