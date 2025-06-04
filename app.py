""" Feedback app Exercise """
from flask import Flask, jsonify, render_template, redirect, session, flash
from models import connect_db, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///auth_exer_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SECRET_KEY'] = 'passwordistaco123'

with app.app_context():
    connect_db(app)
    db.create_all()


# ---------------- #
# Routes for Users #
# ---------------- #

