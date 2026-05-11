# College ERP System

A lightweight Enterprise Resource Planning (ERP) system for colleges and educational institutions. This system manages admissions, fee collection, hostel allocation, examination records, and provides administrative dashboards.

## Features

- **Student Admissions:** Manage student applications, registration, and admissions.
- **Fee Management:** Track fee structures, collect payments, and generate receipts.
- **Hostel Management:** Allocate hostel rooms, monitor occupancy, and track vacancies.
- **Examination System:** Schedule exams, record results, and calculate grades.
- **Administrative Dashboard:** View real-time statistics and reports.
- **Role-based Access Control:** Different access levels for administrators, staff, and students.

## Technology Stack

- **Backend:** Flask (Python web framework)
- **Database:** SQLite (easily replaceable with MySQL/PostgreSQL for production)
- **Frontend:** Bootstrap 5, HTML, CSS, JavaScript
- **Authentication:** Flask-Login
- **Forms:** Flask-WTF
- **ORM:** Flask-SQLAlchemy
- **Migrations:** Flask-Migrate
- **Encryption:** Flask-Bcrypt

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/college-erp.git
cd college-erp
```

2. **Create and activate a virtual environment:**

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**

```bash
# On Windows
set FLASK_APP=run.py
set FLASK_ENV=development
set SECRET_KEY=your_secret_key_here

# On macOS/Linux
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY=your_secret_key_here
```

5. **Initialize the database:**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Run the application:**

```bash
flask run
```

7. **Access the application:**

Open your browser and navigate to `http://127.0.0.1:5000`

## Initial Setup

1. After starting the application, register a new admin user.
2. Access the admin panel to configure:
   - Courses
   - Fee structures
   - Hostel buildings and rooms

## Project Structure

```
college_erp/
│
├── app/                        # Application package
│   ├── models/                 # Database models
│   ├── routes/                 # Route handlers
│   │   ├── admission/          # Admission module
│   │   ├── auth/               # Authentication module
│   │   ├── dashboard/          # Dashboard module
│   │   ├── examination/        # Examination module
│   │   ├── fees/               # Fees module
│   │   ├── hostel/             # Hostel module
│   │   └── main/               # Main routes
│   ├── static/                 # Static files (CSS, JS)
│   ├── templates/              # HTML templates
│   └── __init__.py             # Application factory
│
├── migrations/                 # Database migrations
├── instance/                   # Instance-specific data
├── requirements.txt            # Project dependencies
└── run.py                      # Application entry point
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask and its extensions
- Bootstrap for the UI components
- All contributors who participate in this project

---

Developed with ❤️ for educational institutions in need of affordable ERP solutions.