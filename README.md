# Amit Mondal - Personal Portfolio Website

A simple Personal Portfolio Website built using **Django, HTML, and CSS**.

This project was created as a Django beginner assignment to practice the basic Django flow:

**Model → View → URL → Template**

---

## Project Description

This portfolio website presents my personal information, skills, projects, and project details.

The project uses Django to manage project information through the database and Django Admin Panel.

---

## Features

- Home Page
- Personal introduction
- Profile picture
- Skills section
- Navigation menu
- Projects Page
- Project cards
- Project Details Page
- GitHub button
- Django Admin Panel
- Add projects from Admin
- Edit projects from Admin
- Delete projects from Admin
- About Page
- Contact section
- Responsive design
- Static CSS files

---

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite
- Git
- GitHub
- Visual Studio Code

---

## Django Concepts Used

This project demonstrates the basic Django flow:

```text
Model
  ↓
View
  ↓
URL
  ↓
Template
  ↓
Browser
```

### Model

The `Project` model stores project information such as:

- Project title
- Project description
- Technology used
- GitHub link

### View

Views fetch project information from the database and send the data to the templates.

### URL

URL patterns are used to create routes for:

- Home
- Projects
- Project Details
- About
- Admin

### Template

HTML templates are used to display the project information and personal information.

### Admin

The Django Admin Panel is used to:

- Add projects
- Edit projects
- Delete projects

---

# Installation and Setup

## 1. Clone the Repository

Open Windows Command Prompt and run:

```cmd
git clone https://github.com/aamitmondal/Django-Beginner-Assignment-Personal-Portfolio.git
```

## 2. Go to the Project Folder

```cmd
cd Django-Beginner-Assignment-Personal-Portfolio
```

## 3. Create Virtual Environment

```cmd
python -m venv venv
```

## 4. Activate Virtual Environment

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

After activation, you should see:

```text
(venv)
```

at the beginning of the terminal.

## 5. Install Required Packages

Install the packages from `requirements.txt`:

```cmd
pip install -r requirements.txt
```

## 6. Run Database Migrations

```cmd
python manage.py migrate
```

## 7. Create Admin User

```cmd
python manage.py createsuperuser
```

Enter your:

- Username
- Email
- Password

when prompted.

## 8. Start the Development Server

```cmd
python manage.py runserver
```

Open the website in your browser:

```text
http://127.0.0.1:8000/
```

---

# Admin Panel

The Django Admin Panel is available at:

```text
http://127.0.0.1:8000/admin/
```

After logging in, projects can be:

- Added
- Edited
- Deleted

---

# Website Pages

## Home

```text
/
```

Full URL:

```text
http://127.0.0.1:8000/
```

The Home page contains:

- My name
- Profile picture
- Introduction
- Skills
- Navigation menu
- Contact section

---

## Projects

```text
/projects/
```

Full URL:

```text
http://127.0.0.1:8000/projects/
```

This page displays all projects stored in the database.

---

## Project Details

Example:

```text
/projects/1/
/projects/2/
```

Full URL example:

```text
http://127.0.0.1:8000/projects/1/
```

The Project Details page displays:

- Project title
- Description
- Technology used
- GitHub link

---

## About

```text
/about/
```

Full URL:

```text
http://127.0.0.1:8000/about/
```

The About page contains information about me and my learning journey.

---

## Admin

```text
/admin/
```

Full URL:

```text
http://127.0.0.1:8000/admin/
```

---

# Author

## Amit Mondal

Django Beginner | Python Developer | Web Development Learner

---

# GitHub Repository

Repository:

https://github.com/aamitmondal/Django-Beginner-Assignment-Personal-Portfolio

---

## License

This project was created for educational and learning purposes.
