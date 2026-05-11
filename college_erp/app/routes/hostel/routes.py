from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.models import Student, Hostel, HostelAllocation
from app.routes.hostel.forms import HostelForm, HostelAllocationForm
from datetime import datetime

hostel_bp = Blueprint('hostel', __name__)

@hostel_bp.route('/hostels')
@login_required
def hostels():
    hostels = Hostel.query.all()
    return render_template('hostel/hostels.html', title='Hostels', hostels=hostels)

@hostel_bp.route('/hostel/new', methods=['GET', 'POST'])
@login_required
def new_hostel():
    form = HostelForm()
    
    if form.validate_on_submit():
        hostel = Hostel(
            name=form.name.data,
            block=form.block.data,
            floor=form.floor.data,
            room_number=form.room_number.data,
            capacity=form.capacity.data,
            gender=form.gender.data
        )
        
        db.session.add(hostel)
        db.session.commit()
        flash('Hostel room added successfully!', 'success')
        return redirect(url_for('hostel.hostels'))
        
    return render_template('hostel/create_hostel.html', title='New Hostel', form=form)

@hostel_bp.route('/hostel/<int:hostel_id>')
@login_required
def view_hostel(hostel_id):
    hostel = Hostel.query.get_or_404(hostel_id)
    allocations = HostelAllocation.query.filter_by(hostel_id=hostel_id, status='active').all()
    
    # Calculate occupancy
    occupancy = len(allocations)
    vacancy = hostel.capacity - occupancy
    
    return render_template('hostel/view_hostel.html', title='View Hostel', 
                           hostel=hostel, allocations=allocations, 
                           occupancy=occupancy, vacancy=vacancy)

@hostel_bp.route('/hostel/allocations')
@login_required
def allocations():
    allocations = HostelAllocation.query.all()
    return render_template('hostel/allocations.html', title='Hostel Allocations', allocations=allocations)

@hostel_bp.route('/hostel/allocation/new', methods=['GET', 'POST'])
@login_required
def new_allocation():
    form = HostelAllocationForm()
    form.student.choices = [(s.id, f"{s.first_name} {s.last_name} ({s.admission_id})") for s in Student.query.all()]
    
    # Filter hostels that have vacancy
    available_hostels = []
    hostels = Hostel.query.all()
    
    for hostel in hostels:
        occupancy = HostelAllocation.query.filter_by(hostel_id=hostel.id, status='active').count()
        if occupancy < hostel.capacity:
            available_hostels.append((hostel.id, f"{hostel.name} - Block {hostel.block}, Room {hostel.room_number} ({occupancy}/{hostel.capacity})"))
    
    form.hostel.choices = available_hostels
    
    if form.validate_on_submit():
        # Check if student already has an active allocation
        existing = HostelAllocation.query.filter_by(student_id=form.student.data, status='active').first()
        
        if existing:
            flash('This student already has an active hostel allocation!', 'danger')
            return redirect(url_for('hostel.allocations'))
        
        # Check hostel capacity
        hostel = Hostel.query.get(form.hostel.data)
        occupancy = HostelAllocation.query.filter_by(hostel_id=hostel.id, status='active').count()
        
        if occupancy >= hostel.capacity:
            flash('This hostel room is already at full capacity!', 'danger')
            return redirect(url_for('hostel.allocations'))
            
        # Check gender match
        student = Student.query.get(form.student.data)
        if student.gender != hostel.gender:
            flash('Gender mismatch between student and hostel block!', 'danger')
            return redirect(url_for('hostel.allocations'))
        
        # Create allocation
        allocation = HostelAllocation(
            student_id=form.student.data,
            hostel_id=form.hostel.data,
            academic_year=form.academic_year.data
        )
        
        db.session.add(allocation)
        db.session.commit()
        flash('Hostel allocation created successfully!', 'success')
        return redirect(url_for('hostel.allocations'))
        
    return render_template('hostel/create_allocation.html', title='New Allocation', form=form)

@hostel_bp.route('/hostel/allocation/<int:allocation_id>/vacate')
@login_required
def vacate_allocation(allocation_id):
    allocation = HostelAllocation.query.get_or_404(allocation_id)
    
    if allocation.status == 'vacated':
        flash('This allocation is already vacated!', 'warning')
    else:
        allocation.status = 'vacated'
        allocation.end_date = datetime.utcnow()
        db.session.commit()
        flash('Hostel room vacated successfully!', 'success')
        
    return redirect(url_for('hostel.allocations'))