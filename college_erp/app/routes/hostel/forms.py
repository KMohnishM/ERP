from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class HostelForm(FlaskForm):
    name = StringField('Hostel Name', validators=[DataRequired()])
    block = StringField('Block', validators=[DataRequired()])
    floor = IntegerField('Floor', validators=[DataRequired()])
    room_number = StringField('Room Number', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired(), NumberRange(min=1)])
    gender = SelectField('Gender', choices=[
        ('male', 'Male'),
        ('female', 'Female')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')


class HostelAllocationForm(FlaskForm):
    student = SelectField('Student', coerce=int, validators=[DataRequired()])
    hostel = SelectField('Hostel Room', coerce=int, validators=[DataRequired()])
    academic_year = IntegerField('Academic Year', validators=[DataRequired()])
    submit = SubmitField('Submit')