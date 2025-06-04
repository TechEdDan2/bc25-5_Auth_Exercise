from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Initialize Flask Extensions
db = SQLAlchemy()
bcrypt = Bcrypt()


# Functions
def connect_db(app):
    """ Connect to the Database """
    db.app = app
    db.init_app(app)

# Model Classes
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=True, unique=True)
    first_name = db.Column(db.String(30), nullable=True)
    last_name = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        """ Show User """
        return f"<User {self.id} {self.username}>"
    
    def serialize(self):
        """ Serialize User """
        return {
            'id': self.id,
            'username': self.username
        }
    
    @classmethod
    def create_user(cls, username, password, email=None, first_name=None, last_name=None):
        """ Create a new user """
        # Hash the password and turn the byte string into a regular string
        hashed_pwd = bcrypt.generate_password_hash(password).decode('utf-8')
        return cls(username=username, password=hashed_pwd, email=email,
                   first_name=first_name, last_name=last_name)
       
    
    @classmethod
    def authenticate(cls, username, password):
        """ Authenticate a user """
        user = cls.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        return False
