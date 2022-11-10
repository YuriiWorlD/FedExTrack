from wtforms import SubmitField, StringField, validators
from flask_wtf import Form


class TrackForm(Form):
    tracking_number = StringField('Please enter tracking number:', [validators.DataRequired()])
    submit = SubmitField('Submit')
