# Job Portal - Django Web Application

A comprehensive job portal web application built with Django that connects job seekers with employers.

## Features

### User Management
- User registration and authentication
- Custom user profiles with photo upload
- Role-based access (Job Seeker/Employer)
- Profile management with skills and experience

### Job Management
- Job posting (Admin only)
- Advanced job search and filtering
- Real-time search functionality
- Job categorization by company and location

### Application System
- Resume upload (PDF, DOC, DOCX)
- Cover letter file upload
- Application tracking and management
- Dashboard for job seekers and employers

### Security Features
- CSRF protection
- File type and size validation
- Admin-only job posting restrictions
- Secure file uploads

## Technology Stack

- **Backend**: Django 6.0, Python 3.14
- **Database**: SQLite (development), PostgreSQL ready
- **Frontend**: HTML5, CSS3, JavaScript
- **File Storage**: Django FileField with organized directories
- **Authentication**: Django's built-in user system

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/job-portal.git
cd job-portal
```

2. Create virtual environment:
```bash
python -m venv env
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install django pillow
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## Usage

### For Job Seekers:
1. Register/Login
2. Complete profile with skills and experience
3. Browse and search jobs
4. Apply with resume and cover letter upload
5. Track applications in dashboard

### For Admins:
1. Access admin panel at `/admin/`
2. Post new jobs
3. Manage applications
4. Download resumes and cover letters

## Project Structure

```
jobportal/
├── accounts/          # User authentication and profiles
├── jobs/             # Job management and applications
├── dashboard/        # User dashboards
├── templates/        # HTML templates
├── static/          # CSS, JavaScript, images
├── media/           # User uploaded files
└── manage.py
```

## API Endpoints

- `/` - Home page with job statistics
- `/jobs/` - Job listings with search
- `/jobs/apply/<id>/` - Job application form
- `/accounts/register/` - User registration
- `/accounts/login/` - User login
- `/accounts/profile/` - User profile management
- `/admin/` - Admin panel (superusers only)

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## License

This project is licensed under the MIT License.

## Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/job-portal