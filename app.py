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
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            form.username.errors = ['Username already exists. Please choose a different one.']
            return render_template('register.html', form=form)
        new_user = User.create_user(username, password, email, first_name, last_name)

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id
        flash('Welcome to the Feedback MicroBlog', 'success')
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
            return redirect(f'/user/{u.username}')
        else:
            form.username.errors = ['Invalid username/password']

    return render_template('login.html', form=form)

@app.route('/secret')
def secret_page():
    """ Show a secret page """
    if 'user_id' not in session:
        flash('You must be logged in to view this page.', 'danger')
        return redirect('/login')
    
    user = User.query.get(session['user_id'])
    return render_template('secret.html', user=user)

@app.route('/user')


@app.route('/user/<username>')
def user_profile(username):
    """ Show user profile """
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User not found', 'danger')
        return redirect('/')
    
    if 'user_id' not in session:
        flash('You must be logged in to view this page.', 'danger')
        return redirect('/login')
    
    return render_template('user_profile.html', user=user)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash('Goodbye')
    return redirect('/')

