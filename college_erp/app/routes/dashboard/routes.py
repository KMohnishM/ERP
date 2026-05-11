from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.models.models import (Student, FeePayment, Hostel, HostelAllocation, 
                              Course, Examination, ExamResult, User, Staff)
from sqlalchemy import func
from app import db
from datetime import datetime, timedelta

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role not in ['admin', 'staff']:
        return render_template('errors/403.html'), 403
        
    # Total counts
    total_students = Student.query.count()
    total_courses = Course.query.count()
    total_staff = Staff.query.count()
    
    # Fee collection stats
    current_year = datetime.utcnow().year
    fee_stats = db.session.query(
        func.sum(FeePayment.amount).label('total_fees')
    ).filter(
        func.extract('year', FeePayment.payment_date) == current_year
    ).first()
    
    total_fees = fee_stats.total_fees if fee_stats.total_fees else 0
    
    # Recent admissions
    recent_admissions = Student.query.order_by(Student.admission_date.desc()).limit(5).all()
    
    # Hostel occupancy
    hostel_stats = db.session.query(
        Hostel.gender, 
        func.sum(Hostel.capacity).label('total_capacity'),
        func.count(HostelAllocation.id).label('occupied')
    ).outerjoin(
        HostelAllocation, 
        (HostelAllocation.hostel_id == Hostel.id) & (HostelAllocation.status == 'active')
    ).group_by(Hostel.gender).all()
    
    hostel_data = {
        'male': {'capacity': 0, 'occupied': 0, 'vacant': 0},
        'female': {'capacity': 0, 'occupied': 0, 'vacant': 0}
    }
    
    for stat in hostel_stats:
        gender = stat.gender
        capacity = stat.total_capacity or 0
        occupied = stat.occupied or 0
        vacant = capacity - occupied
        
        hostel_data[gender]['capacity'] = capacity
        hostel_data[gender]['occupied'] = occupied
        hostel_data[gender]['vacant'] = vacant
    
    # Monthly fee collection for current year
    monthly_fees = db.session.query(
        func.extract('month', FeePayment.payment_date).label('month'),
        func.sum(FeePayment.amount).label('amount')
    ).filter(
        func.extract('year', FeePayment.payment_date) == current_year
    ).group_by(
        func.extract('month', FeePayment.payment_date)
    ).all()
    
    fee_data = [0] * 12  # Initialize with zeros for all months
    
    for item in monthly_fees:
        month_idx = int(item.month) - 1  # Convert to 0-based index
        fee_data[month_idx] = float(item.amount)
    
    return render_template('dashboard/dashboard.html', title='Dashboard',
                          total_students=total_students,
                          total_courses=total_courses,
                          total_staff=total_staff,
                          total_fees=total_fees,
                          recent_admissions=recent_admissions,
                          hostel_data=hostel_data,
                          fee_data=fee_data)

@dashboard_bp.route('/api/dashboard/fee-data')
@login_required
def api_fee_data():
    if current_user.role not in ['admin', 'staff']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    current_year = datetime.utcnow().year
    monthly_fees = db.session.query(
        func.extract('month', FeePayment.payment_date).label('month'),
        func.sum(FeePayment.amount).label('amount')
    ).filter(
        func.extract('year', FeePayment.payment_date) == current_year
    ).group_by(
        func.extract('month', FeePayment.payment_date)
    ).all()
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fee_data = [0] * 12  # Initialize with zeros for all months
    
    for item in monthly_fees:
        month_idx = int(item.month) - 1  # Convert to 0-based index
        fee_data[month_idx] = float(item.amount)
    
    data = {
        'labels': months,
        'datasets': [{
            'label': 'Fee Collection',
            'data': fee_data,
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'borderColor': 'rgba(54, 162, 235, 1)',
            'borderWidth': 1
        }]
    }
    
    return jsonify(data)

@dashboard_bp.route('/api/dashboard/hostel-data')
@login_required
def api_hostel_data():
    if current_user.role not in ['admin', 'staff']:
        return jsonify({'error': 'Unauthorized'}), 403
    
    hostel_stats = db.session.query(
        Hostel.gender, 
        func.sum(Hostel.capacity).label('total_capacity'),
        func.count(HostelAllocation.id).label('occupied')
    ).outerjoin(
        HostelAllocation, 
        (HostelAllocation.hostel_id == Hostel.id) & (HostelAllocation.status == 'active')
    ).group_by(Hostel.gender).all()
    
    labels = []
    occupied_data = []
    vacant_data = []
    
    for stat in hostel_stats:
        gender = 'Male' if stat.gender == 'male' else 'Female'
        capacity = stat.total_capacity or 0
        occupied = stat.occupied or 0
        vacant = capacity - occupied
        
        labels.append(gender)
        occupied_data.append(occupied)
        vacant_data.append(vacant)
    
    data = {
        'labels': labels,
        'datasets': [
            {
                'label': 'Occupied',
                'data': occupied_data,
                'backgroundColor': 'rgba(255, 99, 132, 0.2)',
                'borderColor': 'rgba(255, 99, 132, 1)',
                'borderWidth': 1
            },
            {
                'label': 'Vacant',
                'data': vacant_data,
                'backgroundColor': 'rgba(75, 192, 192, 0.2)',
                'borderColor': 'rgba(75, 192, 192, 1)',
                'borderWidth': 1
            }
        ]
    }
    
    return jsonify(data)