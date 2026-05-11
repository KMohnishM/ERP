from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange
from wtforms.fields import DateField

class ExaminationForm(FlaskForm):
    name = StringField('Examination Name', validators=[DataRequired()])
    course = SelectField('Course', coerce=int, validators=[DataRequired()])
    exam_date = DateField('Exam Date', validators=[DataRequired()], format='%Y-%m-%d')
    semester = IntegerField('Semester', validators=[DataRequired(), NumberRange(min=1, max=8)])
    academic_year = IntegerField('Academic Year', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ExamResultForm(FlaskForm):
    student = SelectField('Student', coerce=int, validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    marks_obtained = FloatField('Marks Obtained', validators=[DataRequired(), NumberRange(min=0)])
    total_marks = FloatField('Total Marks', validators=[DataRequired(), NumberRange(min=0)])
    submit = SubmitField('Submit')