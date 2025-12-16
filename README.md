<h1 align="center">Job Portal – Django Web Application</h1>

<p align="center">
  A full-stack job portal web application built with Django that efficiently connects job seekers and employers.
</p>

<hr>

<h2>📌 Overview</h2>
<p>
This Job Portal application allows users to register as job seekers or employers, search and apply for jobs,
upload resumes and cover letters, and manage applications through a secure dashboard.
Admins have full control over job postings and application management.
</p>

<hr>

<h2>✨ Key Features</h2>

<h3>👤 User Management</h3>
<ul>
  <li>User registration and authentication</li>
  <li>Role-based access (Job Seeker / Employer)</li>
  <li>Profile management with skills and experience</li>
  <li>Profile photo upload</li>
</ul>

<h3>💼 Job Management</h3>
<ul>
  <li>Admin-only job posting</li>
  <li>Advanced job search and filtering</li>
  <li>Location and company-based categorization</li>
  <li>Real-time job listing updates</li>
</ul>

<h3>📄 Application System</h3>
<ul>
  <li>Resume upload (PDF, DOC, DOCX)</li>
  <li>Cover letter upload</li>
  <li>Application tracking dashboard</li>
  <li>Employer access to applicant documents</li>
</ul>

<h3>🔐 Security</h3>
<ul>
  <li>CSRF protection</li>
  <li>Secure authentication system</li>
  <li>File type and size validation</li>
  <li>Restricted admin operations</li>
</ul>

<hr>

<h2>🛠 Technology Stack</h2>
<ul>
  <li><strong>Backend:</strong> Django, Python</li>
  <li><strong>Frontend:</strong> HTML5, CSS3, JavaScript</li>
  <li><strong>Database:</strong> SQLite (Development), PostgreSQL (Production Ready)</li>
  <li><strong>Authentication:</strong> Django Authentication System</li>
  <li><strong>File Handling:</strong> Django FileField</li>
</ul>

<hr>

<h2>⚙️ Installation & Setup</h2>

<pre>
git clone https://github.com/yourusername/django-job-portal.git
cd django-job-portal
</pre>

<h4>Create Virtual Environment</h4>
<pre>
python -m venv env
source env/bin/activate      # Linux / Mac
env\Scripts\activate         # Windows
</pre>

<h4>Install Dependencies</h4>
<pre>
pip install django pillow
</pre>

<h4>Run Migrations</h4>
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h4>Create Superuser</h4>
<pre>
python manage.py createsuperuser
</pre>

<h4>Run Development Server</h4>
<pre>
python manage.py runserver
</pre>

<hr>

<h2>🚀 Usage</h2>

<h3>For Job Seekers</h3>
<ul>
  <li>Register and login</li>
  <li>Complete profile</li>
  <li>Search and apply for jobs</li>
  <li>Upload resume and cover letter</li>
  <li>Track applications</li>
</ul>

<h3>For Admins</h3>
<ul>
  <li>Login via <code>/admin/</code></li>
  <li>Create and manage job listings</li>
  <li>View and download applications</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
jobportal/
│── accounts/        # Authentication and user profiles
│── jobs/            # Job postings and applications
│── dashboard/       # User dashboards
│── templates/       # HTML templates
│── static/          # CSS, JS, images
│── media/           # Uploaded resumes and files
│── manage.py
</pre>

<hr>

<h2>🔗 Important Routes</h2>
<ul>
  <li><code>/</code> – Home page</li>
  <li><code>/jobs/</code> – Job listings</li>
  <li><code>/jobs/apply/&lt;id&gt;/</code> – Apply for job</li>
  <li><code>/accounts/register/</code> – User registration</li>
  <li><code>/accounts/login/</code> – User login</li>
  <li><code>/admin/</code> – Admin panel</li>
</ul>

<hr>

<h2>🤝 Contributing</h2>
<ol>
  <li>Fork the repository</li>
  <li>Create a feature branch</li>
  <li>Commit your changes</li>
  <li>Push to the branch</li>
  <li>Open a Pull Request</li>
</ol>

<hr>

<h2>📜 License</h2>
<p>This project is licensed under the <strong>MIT License</strong>.</p>

<hr>

<h2>📬 Contact</h2>
<p>
<strong>Name:</strong> Ankit Avaragol <br>
<strong>Email:</strong> ankitavaragol@gmail.com <br>
<strong>GitHub:</strong> https://github.com/Ankit-03671
</p>
