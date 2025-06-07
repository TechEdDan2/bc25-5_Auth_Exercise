# Auth Exercise - Repo bc25-5_Auth_Exercise

A Flask application demonstrating user authentication, password hashing, and user profile management and nothing more. 

## Table of Contents

- [Overview](#overview)
  - [Features](#features)
  - [Screenshot](#screenshot)
  - [Setup Instructions](#setup-instructions)
- [My Process](#my-process)
  - [File Structure](#file-structure)
  - [Built With](#built-with)
  - [Notes](#notes)
- [Author](#author)
- [License](#license)

## Overview
For this exercise, I create a Flask Feedback application that lets users sign up and log in to their own accounts. Once logged in, users can add feedback, edit their feedback, delete their feedback, and see a list of all feedback that they’ve given. Many of these routes should be protected, so that for example user1 can’t edit a piece of feedback that user2 created.

### Features

- User registration with hashed passwords
- User login and logout
- User profile page (shows all user info except password)
- Session-based authentication
- Feedback model (example of related data)
- Secure routes (only logged-in users can access certain pages)

### Screenshot
![Screenshot of the Flask Feedback Auth Exercise](/static/images/Screenshot.png)

### Setup Instructions

1. **Clone the repository**  
   ```sh
   git clone <repo-url>
   cd Auth_Exercise
   ```

2. **Create and activate a virtual environment**  
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Set up the database**  
   Make sure you have PostgreSQL running and create a database named `auth_exer_db`:
   ```sh
   createdb auth_exer_db
   ```

5. **Run the application**  
   ```sh
   flask run
   ```

6. **Visit the app**  
   Open [http://localhost:5000](http://localhost:5000) in your browser.

## My process

### File Structure

- `app.py` — Main Flask application and routes
- `models.py` — SQLAlchemy models and authentication logic
- `forms.py` — WTForms for registration and login
- `templates/` — HTML templates
- `static/images/` - Location of Screenshot
- `requirements.txt` — Python dependencies

### Built using
 
- Python 3
- Flask
- Flask-Bcrypt
- Flask-WTF
- Flask-SQLAlchemy
- PostgreSQL
- Bootstrap 5

### Notes

- User passwords are securely hashed using Flask-Bcrypt.
- Only logged-in users can view user profiles and secret pages.
- Feedback model is included as an example of a related model.

## Author

- Frontend Mentor - [@TechEdDan2](https://www.frontendmentor.io/profile/TechEdDan2)

## License

This project is licensed under GNU General Public License (GPL) v3