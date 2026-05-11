from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields import DateField

class AdmissionForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    date_of_birth = DateField('Date of Birth', validators=[DataRequired()], format='%Y-%m-%d')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    address = TextAreaField('Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=15)])
    course = SelectField('Course', coerce=int, validators=[DataRequired()])
    batch_year = IntegerField('Batch Year', validators=[DataRequired()])
    submit = SubmitField('Submit')