from flask import render_template

from app import app
from app.models import User, Vote, Seminar

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', title = 'Home', users=users)

@app.route('/vote')
def vote():
    return render_template('vote.html', title = 'Vote')

