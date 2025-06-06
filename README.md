# Auth Exercise - Repo bc25-5_Auth_Exercise

A Flask application demonstrating user authentication, password hashing, and user profile management and nothing more. 

## Table of contents

- [Overview](#overview)
  - [Features](#features)
  - [Screenshot](#screenshot)
  - [Setup](#setup-instructions)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)
  - [Continued development](#continued-development)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview
For this exercise, I create a Flask Feedback application that lets users sign up and log in to their own accounts. Once logged in, users can add feedback, edit their feedback, delete their feedback, and see a list of all feedback that they’ve given. Many of these routes should be protected, so that for example user1 can’t edit a piece of feedback that user2 created.

### Features

- User registration with hashed passwords
- User login and logout
- User profile page (shows all user info except password)
- Session-based authentication
- Feedback model (example of related data)
- Secure routes (only logged-in users can access certain pages)

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

## File Structure

- `app.py` — Main Flask application and routes
- `models.py` — SQLAlchemy models and authentication logic
- `forms.py` — WTForms for registration and login
- `templates/` — HTML templates
- `requirements.txt` — Python dependencies

## Notes

- User passwords are securely hashed using Flask-Bcrypt.
- Only logged-in users can view user profiles and secret pages.
- Feedback model is included as an example of a related model.
