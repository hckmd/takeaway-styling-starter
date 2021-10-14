from flask import render_template, request, redirect, url_for

from app import app, db
from app.models import User, Vote, Seminar
from app.forms import AddVoteForm, EditSeminar
from sqlalchemy import desc
from sqlalchemy.sql.expression import null
from datetime import date

def get_users():
    # A helper function that returns a list of tuples with user ids and names from the user table.
    # Used to populate the User dropdown for voting.
    players = [(player.id, player.name) for player in User.query.all()]
    return players

def get_seminars():
    # A helper function that returns a list of seminars table.
    seminars = [(seminar.id, seminar.week) for seminar in Seminar.query.filter_by(finish=None)]
    return seminars

@app.route('/')
@app.route('/index')
def index():
    users = User.query.order_by(User.score)
    return render_template('index.html', title = 'Home', users=users)

@app.route('/vote', methods = ['GET', 'POST'])
def vote():
    form = AddVoteForm()
    # gets the choices for the current Tribals
    form.user_id.choices = get_users()
    # gets the choices for the contestants form field
    form.seminar_id.choices = get_seminars()
    # Check if the form has been submitted (is a POST request) and form inputs are valid
    if form.validate_on_submit():
        # The form has been submitted and the inputs are valid
        vote = Vote()
        form.populate_obj(obj=vote)
        # Adds the vote object to session for creation and saves changes to db
        db.session.add(vote)
        db.session.commit()
        
        return render_template('vote_successful.html', vote = vote, title="Vote Placed")

    return render_template('vote.html', form = form, title='Vote')

@app.route('/admin')
def admin():
    # Retrieve all seminars 
    seminars = Seminar.query.filter_by(finish=None)

    return render_template('admin.html', seminars=seminars)

@app.route('/edit_seminar/<int:id>', methods = ['GET', 'POST'])
def edit_seminar(id):

    seminar = Seminar.query.get_or_404(id)
    form = EditSeminar(obj=seminar)

    # Check if the form has been submitted (is a POST request) and form inputs are valid
    if form.validate_on_submit():
        # The form has been submitted and the inputs are valid
        form.populate_obj(obj=seminar)

        # Update user scores
        finish_min = seminar.finish
        votes = Vote.query.filter_by(seminar_id=id)
        for item in votes:
            user = item.user
            user.score += (abs(item.minutes_over - finish_min))
        
        db.session.commit()
        
        return redirect(url_for('index'))
    seminar_week = f'week {seminar.week} on {seminar.seminar_date}'
    return render_template('edit_seminar.html', form = form, seminar_week = seminar_week, title='Add Seminar End Time')