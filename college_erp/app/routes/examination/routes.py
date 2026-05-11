from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Student, Course, Examination, ExamResult
from app.routes.examination.forms import ExaminationForm, ExamResultForm
from datetime import datetime

exam_bp = Blueprint('exam', __name__)

@exam_bp.route('/examinations')
@login_required
def examinations():
    exams = Examination.query.all()
    return render_template('examination/examinations.html', title='Examinations', exams=exams)

@exam_bp.route('/examination/new', methods=['GET', 'POST'])
@login_required
def new_examination():
    form = ExaminationForm()
    form.course.choices = [(c.id, f"{c.name} ({c.code})") for c in Course.query.all()]
    
    if form.validate_on_submit():
        exam = Examination(
            name=form.name.data,
            course_id=form.course.data,
            exam_date=form.exam_date.data,
            semester=form.semester.data,
            academic_year=form.academic_year.data
        )
        
        db.session.add(exam)
        db.session.commit()
        flash('Examination added successfully!', 'success')
        return redirect(url_for('exam.examinations'))
        
    return render_template('examination/create_examination.html', title='New Examination', form=form)

@exam_bp.route('/examination/<int:exam_id>')
@login_required
def view_examination(exam_id):
    exam = Examination.query.get_or_404(exam_id)
    results = ExamResult.query.filter_by(examination_id=exam_id).all()
    
    return render_template('examination/view_examination.html', title='View Examination', 
                           exam=exam, results=results)

@exam_bp.route('/examination/<int:exam_id>/add-result', methods=['GET', 'POST'])
@login_required
def add_result(exam_id):
    exam = Examination.query.get_or_404(exam_id)
    form = ExamResultForm()
    
    # Get students for this course only
    students = Student.query.filter_by(course_id=exam.course_id).all()
    form.student.choices = [(s.id, f"{s.first_name} {s.last_name} ({s.admission_id})") for s in students]
    
    if form.validate_on_submit():
        # Check if result already exists
        existing = ExamResult.query.filter_by(
            student_id=form.student.data,
            examination_id=exam_id,
            subject=form.subject.data
        ).first()
        
        if existing:
            flash('Result for this student and subject already exists!', 'danger')
            return redirect(url_for('exam.view_examination', exam_id=exam_id))
        
        # Calculate grade based on marks
        marks_percentage = (form.marks_obtained.data / form.total_marks.data) * 100
        
        if marks_percentage >= 90:
            grade = 'A+'
        elif marks_percentage >= 80:
            grade = 'A'
        elif marks_percentage >= 70:
            grade = 'B+'
        elif marks_percentage >= 60:
            grade = 'B'
        elif marks_percentage >= 50:
            grade = 'C'
        elif marks_percentage >= 40:
            grade = 'D'
        else:
            grade = 'F'
        
        result = ExamResult(
            student_id=form.student.data,
            examination_id=exam_id,
            subject=form.subject.data,
            marks_obtained=form.marks_obtained.data,
            total_marks=form.total_marks.data,
            grade=grade
        )
        
        db.session.add(result)
        db.session.commit()
        flash('Result added successfully!', 'success')
        return redirect(url_for('exam.view_examination', exam_id=exam_id))
        
    return render_template('examination/add_result.html', title='Add Result', 
                           form=form, exam=exam)

@exam_bp.route('/student/<int:student_id>/results')
@login_required
def student_results(student_id):
    student = Student.query.get_or_404(student_id)
    results = ExamResult.query.filter_by(student_id=student_id).all()
    
    # Group results by examination
    grouped_results = {}
    for result in results:
        exam_id = result.examination_id
        if exam_id not in grouped_results:
            grouped_results[exam_id] = {
                'exam': result.examination,
                'results': []
            }
        grouped_results[exam_id]['results'].append(result)
    
    return render_template('examination/student_results.html', title='Student Results',
                           student=student, grouped_results=grouped_results)