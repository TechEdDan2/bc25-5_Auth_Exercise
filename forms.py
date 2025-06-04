from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, Email, Optional

class LoginForm(FlaskForm):
    """ Form for creating or updating a user """
    
    # Fields for the form 
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    # submit = SubmitField('Submit')
    
class RegForm(FlaskForm):
    """ Form for creating or updating a user """
    
    # Fields for the form 
    username = StringField('Username', validators=[InputRequired(), Length(max=20)])
    password = PasswordField('Password', validators=[InputRequired()])
    email =  EmailField('Email', validators=[Optional(), Length(max=50)])
    first_name = StringField('First Name', validators=[Optional(), Length(max=30)])
    last_name = StringField('Last Name', validators=[Optional(), Length(max=30)])
    # submit = SubmitField('Submit')


class FeedbackForm(FlaskForm):
    """ This for is used for creating posts """

    # Fields for the form
    text = StringField("Feedback", validators=[InputRequired()])