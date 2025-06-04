""" Feedback app Exercise """
from flask import Flask, jsonify, render_template, redirect, session, flash
from models import connect_db, db, User
from forms import LoginForm, RegForm

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
@app.route('/')
def index():
    """ Show the homepage """
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def registerUser():
    form = RegForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        new_user = User.create_user(username, password)

        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Welcome to MyMicroBlogging!', 'success')
        return redirect('/posts')
    return render_template('register.html', form = form)

@app.route('/login', methods=["GET", "POST"])
def login_user():
    form = LoginForm()

    # Logic for POST Request
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        u = User.authenticate(username,password)

        if u:
            flash(f"Welcome Back, {u.username}!", "success")
            session['user_id'] = u.id
            return redirect('/posts')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form= form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash('Goodbye')
    return redirect('/')
