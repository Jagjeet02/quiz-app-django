# quiz-app-django
# Django Quiz App

## Features
- Start a new quiz session
- Answer random questions from the database
- View quiz summary (Total, Correct, Incorrect)
- **Enhancements**: Timer, Leaderboard (optional)

## Requirements
- Python 3.x
- Django
- Gunicorn (for production deployment)


**Instructions to Run the Django Quiz App Project**
**Clone the repository:**
git clone https://github.com/Jagjeet02/quiz-app-django.git
cd quiz-app-django
**Set up a virtual environment:**

For Windows:
python -m venv venv
venv\Scripts\activate
For Mac/Linux:
python3 -m venv venv
source venv/bin/activate

**Install project dependencies:**
pip install -r requirements.txt

**Run database migrations to set up the database:**
python manage.py makemigrations
python manage.py migrate

**Run the development server:**
python manage.py runserver

**Access the application:**
Open a browser and go to:
arduino
Copy code
http://127.0.0.1:8000
Notes:
Make sure you have Python 3.8+ installed.
If requirements.txt does not exist, install Django manually:
pip install django
