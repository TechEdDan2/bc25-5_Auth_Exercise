from app import app
from models import db, User, Feedback

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    #Create Sample users
    test_user1 = User.create_user(
        username="asoka",
        password="jedi",
        email="rosarioD@example.com",
        first_name="Asoka",
        last_name="Tano"
    )

    test_user2 = User.create_user(
        username="baymax",
        password="healthcare",
        email="hero6@example.com",
        first_name="Baymax",
        last_name="Personal Healthcare Robot"
    )

    db.session.add_all([test_user1, test_user2])
    db.session.commit()

    # Create sample feedback
    feedback1 = Feedback(
        title="Hello Universe",
        content="I am no Jedi",
        user_id=test_user1.id,
        username=test_user1.username
    )
    feedback2 = Feedback(
        title="Balalala lalalala!",
        content="Hello, I am Baymax, your personal healthcare companion.",
        user_id=test_user2.id,
        username=test_user2.username
    )

    db.session.add_all([feedback1, feedback2])
    db.session.commit()

    print("Database seeded!")