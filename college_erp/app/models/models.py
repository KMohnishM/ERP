from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='staff')  # 'admin', 'staff', 'student'
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    student = db.relationship('Student', backref='user', uselist=False)
    staff = db.relationship('Staff', backref='user', uselist=False)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.role}')"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    admission_id = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    address = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    batch_year = db.Column(db.Integer, nullable=False)
    admission_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationships
    course = db.relationship('Course', backref='students')
    fees = db.relationship('FeePayment', backref='student', lazy=True)
    hostel_allocation = db.relationship('HostelAllocation', backref='student', uselist=False)
    exam_results = db.relationship('ExamResult', backref='student', lazy=True)
    
    def __repr__(self):
        return f"Student('{self.admission_id}', '{self.first_name}', '{self.last_name}')"


class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    staff_id = db.Column(db.String(20), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    designation = db.Column(db.String(50), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    joining_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f"Staff('{self.staff_id}', '{self.first_name}', '{self.last_name}', '{self.designation}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    duration_years = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Course('{self.code}', '{self.name}')"


class FeeStructure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    academic_year = db.Column(db.Integer, nullable=False)
    tuition_fee = db.Column(db.Float, nullable=False)
    exam_fee = db.Column(db.Float, nullable=False)
    hostel_fee = db.Column(db.Float, nullable=False)
    other_fee = db.Column(db.Float, nullable=False)
    
    course = db.relationship('Course', backref='fee_structures')
    
    def __repr__(self):
        return f"FeeStructure(Course: '{self.course.name}', Year: {self.academic_year})"


class FeePayment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    fee_type = db.Column(db.String(50), nullable=False)  # 'tuition', 'exam', 'hostel', 'other'
    amount = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    receipt_number = db.Column(db.String(20), unique=True, nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)  # 'cash', 'online', 'bank'
    academic_year = db.Column(db.Integer, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"FeePayment('{self.receipt_number}', '{self.fee_type}', {self.amount})"


class Hostel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    block = db.Column(db.String(10), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(10), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)  # 'male', 'female'
    
    # Relationship
    allocations = db.relationship('HostelAllocation', backref='hostel', lazy=True)
    
    def __repr__(self):
        return f"Hostel('{self.name}', '{self.block}', '{self.room_number}')"


class HostelAllocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    hostel_id = db.Column(db.Integer, db.ForeignKey('hostel.id'), nullable=False)
    allotment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_date = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(20), nullable=False, default='active')  # 'active', 'vacated'
    academic_year = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"HostelAllocation(Student: {self.student_id}, Hostel: {self.hostel_id}, Status: {self.status})"


class Examination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    exam_date = db.Column(db.Date, nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    academic_year = db.Column(db.Integer, nullable=False)
    
    # Relationship
    course = db.relationship('Course', backref='examinations')
    results = db.relationship('ExamResult', backref='examination', lazy=True)
    
    def __repr__(self):
        return f"Examination('{self.name}', '{self.course.name}', Semester: {self.semester})"


class ExamResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    examination_id = db.Column(db.Integer, db.ForeignKey('examination.id'), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    marks_obtained = db.Column(db.Float, nullable=False)
    total_marks = db.Column(db.Float, nullable=False)
    grade = db.Column(db.String(5), nullable=False)
    
    def __repr__(self):
        return f"ExamResult(Student: {self.student_id}, Subject: '{self.subject}', Marks: {self.marks_obtained})"