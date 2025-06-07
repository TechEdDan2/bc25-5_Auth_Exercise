""" Feedback app Exercise """
from flask import Flask, jsonify, render_template, redirect, session, flash
from models import connect_db, db, User, Feedback
from forms import LoginForm, RegForm, FeedbackForm

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
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return render_template('index.html', user=user)

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
        return redirect('/user/' + new_user.username)
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

# @app.route('/user')


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

@app.route('/feedback' , methods=['GET', 'POST'])
def feedback_list():
    """ Show all feedback """
    # GET Logic
    if 'user_id' not in session:
        flash('You must be logged in to view this page.', 'danger')
        return redirect('/login')
    
    form = FeedbackForm()
    feedbacks = Feedback.query.all()
    user = User.query.get(session['user_id'])
    
    # POST Logic
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        user_id = session['user_id']
        username = User.query.get(user_id).username
        
        new_feedback = Feedback(title=title, content=content, user_id=user_id, username=username)
        
        db.session.add(new_feedback)
        db.session.commit()
        
        flash('Feedback submitted successfully!', 'success')
        return redirect('/feedback')
    
    
    return render_template('feedback.html', feedbacks=feedbacks, form=form, user=user)

@app.route('/feedback/<int:id>/delete', methods=['POST'])
def delete_feedback(id):
    """ Delete feedback by ID """
    feedback = Feedback.query.get_or_404(id)
    
    if 'user_id' not in session or session['user_id'] != feedback.user_id:
        flash('You do not have permission to delete this feedback.', 'danger')
        return redirect('/feedback')
    
    db.session.delete(feedback)
    db.session.commit()
    
    flash('Feedback deleted successfully!', 'success')
    return redirect('/feedback')

@app.route('/feedback/<int:id>/edit', methods=['GET', 'POST'])
def edit_feedback(id):
    """ Edit feedback by ID """
    feedback = Feedback.query.get_or_404(id)
    
    if 'user_id' not in session or session['user_id'] != feedback.user_id:
        flash('You do not have permission to edit this feedback.', 'danger')
        return redirect('/feedback')
    
    user = User.query.get(session['user_id'])
    form = FeedbackForm(obj=feedback)
    
    if form.validate_on_submit():
        feedback.title = form.title.data
        feedback.content = form.content.data
        
        db.session.commit()
        
        flash('Feedback updated successfully!', 'success')
        return redirect('/feedback')
    
    return render_template('feedback_edit.html', form=form, feedback=feedback, user=user)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    flash('Goodbye')
    return redirect('/')

