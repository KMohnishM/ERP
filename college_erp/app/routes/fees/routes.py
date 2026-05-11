from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Student, FeePayment, FeeStructure, Course
from app.routes.fees.forms import FeePaymentForm, FeeStructureForm
import uuid
from datetime import datetime

fees_bp = Blueprint('fees', __name__)

@fees_bp.route('/fees')
@login_required
def fees():
    fee_payments = FeePayment.query.all()
    return render_template('fees/fees.html', title='Fee Payments', fee_payments=fee_payments)

@fees_bp.route('/fees/structures')
@login_required
def fee_structures():
    structures = FeeStructure.query.all()
    return render_template('fees/fee_structures.html', title='Fee Structures', structures=structures)

@fees_bp.route('/fees/structure/new', methods=['GET', 'POST'])
@login_required
def new_fee_structure():
    form = FeeStructureForm()
    form.course.choices = [(c.id, f"{c.name} ({c.code})") for c in Course.query.all()]
    
    if form.validate_on_submit():
        fee_structure = FeeStructure(
            course_id=form.course.data,
            academic_year=form.academic_year.data,
            tuition_fee=form.tuition_fee.data,
            exam_fee=form.exam_fee.data,
            hostel_fee=form.hostel_fee.data,
            other_fee=form.other_fee.data
        )
        
        db.session.add(fee_structure)
        db.session.commit()
        flash('Fee structure added successfully!', 'success')
        return redirect(url_for('fees.fee_structures'))
        
    return render_template('fees/create_fee_structure.html', title='New Fee Structure', form=form)

@fees_bp.route('/fees/payment/new', methods=['GET', 'POST'])
@login_required
def new_payment():
    form = FeePaymentForm()
    form.student.choices = [(s.id, f"{s.first_name} {s.last_name} ({s.admission_id})") for s in Student.query.all()]
    
    if form.validate_on_submit():
        # Generate a unique receipt number
        receipt_number = f"RCP-{uuid.uuid4().hex[:6].upper()}"
        
        fee_payment = FeePayment(
            student_id=form.student.data,
            fee_type=form.fee_type.data,
            amount=form.amount.data,
            receipt_number=receipt_number,
            payment_method=form.payment_method.data,
            academic_year=form.academic_year.data,
            semester=form.semester.data
        )
        
        db.session.add(fee_payment)
        db.session.commit()
        flash(f'Payment recorded successfully! Receipt Number: {receipt_number}', 'success')
        return redirect(url_for('fees.fees'))
        
    return render_template('fees/create_payment.html', title='New Payment', form=form)

@fees_bp.route('/fees/payment/<int:payment_id>')
@login_required
def view_payment(payment_id):
    payment = FeePayment.query.get_or_404(payment_id)
    return render_template('fees/view_payment.html', title='View Payment', payment=payment)

@fees_bp.route('/fees/student/<int:student_id>')
@login_required
def student_fees(student_id):
    student = Student.query.get_or_404(student_id)
    fee_payments = FeePayment.query.filter_by(student_id=student_id).all()
    
    return render_template('fees/student_fees.html', title='Student Fees', student=student, fee_payments=fee_payments)