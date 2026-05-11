from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class FeePaymentForm(FlaskForm):
    student = SelectField('Student', coerce=int, validators=[DataRequired()])
    fee_type = SelectField('Fee Type', choices=[
        ('tuition', 'Tuition Fee'),
        ('exam', 'Examination Fee'),
        ('hostel', 'Hostel Fee'),
        ('other', 'Other Fee')
    ], validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0)])
    payment_method = SelectField('Payment Method', choices=[
        ('cash', 'Cash'),
        ('online', 'Online Transfer'),
        ('bank', 'Bank Deposit')
    ], validators=[DataRequired()])
    academic_year = IntegerField('Academic Year', validators=[DataRequired()])
    semester = IntegerField('Semester', validators=[DataRequired(), NumberRange(min=1, max=8)])
    submit = SubmitField('Submit')


class FeeStructureForm(FlaskForm):
    course = SelectField('Course', coerce=int, validators=[DataRequired()])
    academic_year = IntegerField('Academic Year', validators=[DataRequired()])
    tuition_fee = FloatField('Tuition Fee', validators=[DataRequired(), NumberRange(min=0)])
    exam_fee = FloatField('Examination Fee', validators=[DataRequired(), NumberRange(min=0)])
    hostel_fee = FloatField('Hostel Fee', validators=[DataRequired(), NumberRange(min=0)])
    other_fee = FloatField('Other Fees', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')