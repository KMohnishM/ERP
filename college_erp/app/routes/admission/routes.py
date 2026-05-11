from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Student, Course, User
from app.routes.admission.forms import AdmissionForm
import uuid
from datetime import datetime

admission_bp = Blueprint('admission', __name__)

@admission_bp.route('/admissions')
@login_required
def admissions():
    students = Student.query.all()
    return render_template('admission/admissions.html', title='Admissions', students=students)

@admission_bp.route('/admission/new', methods=['GET', 'POST'])
@login_required
def new_admission():
    form = AdmissionForm()
    form.course.choices = [(c.id, f"{c.name} ({c.code})") for c in Course.query.all()]
    
    if form.validate_on_submit():
        # Generate a unique admission ID
        admission_id = f"ADM-{uuid.uuid4().hex[:6].upper()}"
        
        # Check if user exists, if not create one
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            # Create a new user with student role
            from app import bcrypt
            password = 'password123'  # Default password
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(username=form.email.data.split('@')[0], 
                        email=form.email.data, 
                        password=hashed_password, 
                        role='student')
            db.session.add(user)
            db.session.flush()
        
        # Create student record
        student = Student(
            user_id=user.id,
            admission_id=admission_id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            date_of_birth=form.date_of_birth.data,
            gender=form.gender.data,
            address=form.address.data,
            phone=form.phone.data,
            course_id=form.course.data,
            batch_year=form.batch_year.data
        )
        
        db.session.add(student)
        db.session.commit()
        flash(f'Admission successful! Admission ID: {admission_id}', 'success')
        return redirect(url_for('admission.admissions'))
        
    return render_template('admission/create_admission.html', title='New Admission', form=form)

@admission_bp.route('/admission/<int:student_id>')
@login_required
def view_admission(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('admission/view_admission.html', title='View Admission', student=student)

@admission_bp.route('/admission/<int:student_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_admission(student_id):
    student = Student.query.get_or_404(student_id)
    form = AdmissionForm()
    form.course.choices = [(c.id, f"{c.name} ({c.code})") for c in Course.query.all()]
    
    if form.validate_on_submit():
        student.first_name = form.first_name.data
        student.last_name = form.last_name.data
        student.date_of_birth = form.date_of_birth.data
        student.gender = form.gender.data
        student.address = form.address.data
        student.phone = form.phone.data
        student.course_id = form.course.data
        student.batch_year = form.batch_year.data
        
        db.session.commit()
        flash('Student information updated successfully!', 'success')
        return redirect(url_for('admission.view_admission', student_id=student.id))
        
    elif request.method == 'GET':
        form.first_name.data = student.first_name
        form.last_name.data = student.last_name
        form.date_of_birth.data = student.date_of_birth
        form.gender.data = student.gender
        form.address.data = student.address
        form.phone.data = student.phone
        form.course.data = student.course_id
        form.batch_year.data = student.batch_year
        form.email.data = student.user.email
        
    return render_template('admission/edit_admission.html', title='Edit Admission', form=form, student=student)