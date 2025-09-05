# Online Examination System (Django)

## Features
- Roles: Admin (create exams/questions), Student (take exams)
- Create MCQ questions, form exams, students take timed exams
- Automatic scoring and result storage
- Simple dashboard and admin integration

## Quick start
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
