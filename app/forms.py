from datetime import date, datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, BooleanField, SelectField, HiddenField, PasswordField, DateField
from wtforms.validators import InputRequired, Length, EqualTo


class AddVoteForm(FlaskForm):
    user_id = SelectField('Seminar:', coerce=int, validators = [InputRequired()])
    seminar_id = SelectField('Your name:', coerce=int, validators = [InputRequired()])
    minutes_over = IntegerField('Your guess (in minutes):')
    submit = SubmitField('Place Vote')