import os
import sys
from datetime import datetime, timedelta
import random
import uuid
from werkzeug.security import generate_password_hash

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the app and models
from app import create_app, db
from app.models.models import (User, Student, Staff, Course, FeeStructure, 
                              FeePayment, Hostel, HostelAllocation, 
                              Examination, ExamResult)

app = create_app()

def create_sample_data():
    with app.app_context():
        print("Creating sample data...")
        
        # Check if data already exists
        if User.query.count() > 0:
            print("Data already exists. Skipping...")
            return
            
        # Create admin user
        admin_user = User(
            username='admin',
            email='admin@college.edu',
            password=generate_password_hash('admin123'),
            role='admin'
        )
        db.session.add(admin_user)
        db.session.flush()
        
        # Create staff user
        staff_user = User(
            username='staff',
            email='staff@college.edu',
            password=generate_password_hash('staff123'),
            role='staff'
        )
        db.session.add(staff_user)
        db.session.flush()
        
        # Create staff profile
        staff = Staff(
            user_id=staff_user.id,
            staff_id=f'STAFF-{uuid.uuid4().hex[:6].upper()}',
            first_name='John',
            last_name='Doe',
            designation='Administrator',
            department='Administration',
            phone='9876543210',
            joining_date=datetime.now() - timedelta(days=365)
        )
        db.session.add(staff)
        
        # Create courses
        courses = [
            Course(code='CSE101', name='Computer Science Engineering', department='Engineering', duration_years=4),
            Course(code='ECE101', name='Electronics Engineering', department='Engineering', duration_years=4),
            Course(code='ME101', name='Mechanical Engineering', department='Engineering', duration_years=4),
            Course(code='BBA101', name='Business Administration', department='Management', duration_years=3),
            Course(code='BSC101', name='Bachelor of Science', department='Science', duration_years=3)
        ]
        
        for course in courses:
            db.session.add(course)
        db.session.flush()
        
        # Create fee structures
        current_year = datetime.now().year
        for course in courses:
            fee_structure = FeeStructure(
                course_id=course.id,
                academic_year=current_year,
                tuition_fee=50000 + random.randint(0, 20000),
                exam_fee=5000,
                hostel_fee=30000,
                other_fee=10000
            )
            db.session.add(fee_structure)
        
        # Create hostels
        hostels = []
        # Male hostels
        for i in range(1, 6):
            for j in range(1, 5):
                hostel = Hostel(
                    name=f'Boys Hostel {i}',
                    block=f'B{i}',
                    floor=j,
                    room_number=f'{j}0{i}',
                    capacity=3,
                    gender='male'
                )
                hostels.append(hostel)
                db.session.add(hostel)
                
        # Female hostels
        for i in range(1, 6):
            for j in range(1, 5):
                hostel = Hostel(
                    name=f'Girls Hostel {i}',
                    block=f'G{i}',
                    floor=j,
                    room_number=f'{j}0{i}',
                    capacity=3,
                    gender='female'
                )
                hostels.append(hostel)
                db.session.add(hostel)
                
        db.session.flush()
        
        # Create student users and admissions
        first_names = ['Alex', 'James', 'Michael', 'Emma', 'Olivia', 'Sophia', 'William', 'Benjamin', 'Ava', 'Mia']
        last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
        domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'hotmail.com']
        
        students = []
        for i in range(30):
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            email = f"{first_name.lower()}.{last_name.lower()}{random.randint(1, 999)}@{random.choice(domains)}"
            gender = random.choice(['male', 'female'])
            course = random.choice(courses)
            batch_year = random.choice([current_year - 1, current_year])
            
            # Create user
            user = User(
                username=f"{first_name.lower()}{random.randint(1, 999)}",
                email=email,
                password=generate_password_hash('student123'),
                role='student'
            )
            db.session.add(user)
            db.session.flush()
            
            # Create student
            student = Student(
                user_id=user.id,
                admission_id=f'ADM-{uuid.uuid4().hex[:6].upper()}',
                first_name=first_name,
                last_name=last_name,
                date_of_birth=datetime.now() - timedelta(days=365 * random.randint(18, 25)),
                gender=gender,
                address=f'{random.randint(1, 999)} Main St, City',
                phone=f'9{random.randint(100000000, 999999999)}',
                course_id=course.id,
                batch_year=batch_year,
                admission_date=datetime.now() - timedelta(days=random.randint(1, 180))
            )
            db.session.add(student)
            db.session.flush()
            students.append(student)
            
            # Create fee payments
            fee_types = ['tuition', 'exam', 'hostel', 'other']
            for fee_type in fee_types:
                if random.random() > 0.3:  # 70% chance of payment
                    if fee_type == 'tuition':
                        amount = 50000 + random.randint(0, 20000)
                    elif fee_type == 'exam':
                        amount = 5000
                    elif fee_type == 'hostel':
                        amount = 30000
                    else:
                        amount = 10000
                        
                    payment = FeePayment(
                        student_id=student.id,
                        fee_type=fee_type,
                        amount=amount,
                        payment_date=datetime.now() - timedelta(days=random.randint(1, 90)),
                        receipt_number=f'RCP-{uuid.uuid4().hex[:6].upper()}',
                        payment_method=random.choice(['cash', 'online', 'bank']),
                        academic_year=current_year,
                        semester=random.randint(1, 2)
                    )
                    db.session.add(payment)
        
        # Create hostel allocations
        male_students = [s for s in students if s.gender == 'male']
        female_students = [s for s in students if s.gender == 'female']
        
        male_hostels = [h for h in hostels if h.gender == 'male']
        female_hostels = [h for h in hostels if h.gender == 'female']
        
        # Allocate male students
        for i, student in enumerate(male_students):
            if i < len(male_hostels):
                hostel = male_hostels[i]
                allocation = HostelAllocation(
                    student_id=student.id,
                    hostel_id=hostel.id,
                    allotment_date=datetime.now() - timedelta(days=random.randint(1, 30)),
                    academic_year=current_year,
                    status='active'
                )
                db.session.add(allocation)
        
        # Allocate female students
        for i, student in enumerate(female_students):
            if i < len(female_hostels):
                hostel = female_hostels[i]
                allocation = HostelAllocation(
                    student_id=student.id,
                    hostel_id=hostel.id,
                    allotment_date=datetime.now() - timedelta(days=random.randint(1, 30)),
                    academic_year=current_year,
                    status='active'
                )
                db.session.add(allocation)
        
        # Create examinations
        for course in courses:
            exam = Examination(
                name=f'Mid Semester Exam - {course.name}',
                course_id=course.id,
                exam_date=datetime.now() - timedelta(days=15),
                semester=1,
                academic_year=current_year
            )
            db.session.add(exam)
            db.session.flush()
            
            # Create exam results for students in this course
            course_students = [s for s in students if s.course_id == course.id]
            subjects = ['Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'English']
            
            for student in course_students:
                for subject in subjects:
                    marks_obtained = random.randint(40, 100)
                    total_marks = 100
                    
                    # Calculate grade
                    percentage = (marks_obtained / total_marks) * 100
                    if percentage >= 90:
                        grade = 'A+'
                    elif percentage >= 80:
                        grade = 'A'
                    elif percentage >= 70:
                        grade = 'B+'
                    elif percentage >= 60:
                        grade = 'B'
                    elif percentage >= 50:
                        grade = 'C'
                    elif percentage >= 40:
                        grade = 'D'
                    else:
                        grade = 'F'
                        
                    result = ExamResult(
                        student_id=student.id,
                        examination_id=exam.id,
                        subject=subject,
                        marks_obtained=marks_obtained,
                        total_marks=total_marks,
                        grade=grade
                    )
                    db.session.add(result)
        
        db.session.commit()
        print("Sample data created successfully!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    create_sample_data()