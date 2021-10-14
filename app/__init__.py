from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

# Set up configuration settings for connection to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///endtime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'this-is-a-endtime-secret' 
db = SQLAlchemy(app)


from app import routes, models, forms

@app.cli.command('init-db')
def init_db():
    # Delete and remake the database 
    db.drop_all()
    db.create_all()

    # Add some sample data for different takeaway items

    troy = models.User (
        name = 'Troy'
    )
    db.session.add(troy)

    kylie = models.User (
        name = 'Kylie'
    )
    db.session.add(kylie)

    michelle = models.User (
        name = 'Michelle'
    )
    db.session.add(michelle)

    kelly = models.User (
        name = 'Kelly'
    )
    db.session.add(kelly)

    kirsty = models.User (
        name = 'Kirsty'
    )
    db.session.add(kirsty)

    mark = models.User (
        name = 'Mark'
    )
    db.session.add(mark)

    sally = models.User (
        name = 'Sally'
    )
    db.session.add(sally)

    week9 = models.Seminar (
        week = 9,
        seminar_date = date(2021,10,14),
        finish = 10
    )
    db.session.add(week9)

    week10 = models.Seminar (
        week = 10,
        seminar_date = date(2021,10,21)
    )
    db.session.add(week10)

    week11 = models.Seminar (
        week = 11,
        seminar_date = date(2021,10,28)
    )
    db.session.add(week11)

    week12 = models.Seminar (
        week = 12,
        seminar_date = date(2021,11,4)
    )
    db.session.add(week12)

    # Save the changes to the database
    db.session.commit()

