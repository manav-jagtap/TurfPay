# TurfPay — Turf Booking Platform

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://neon.com/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat-square&logo=render&logoColor=black)](https://turfpay.onrender.com/)

TurfPay is a web-based turf discovery and booking platform built for sports players and turf owners in Latur.

The platform helps customers explore local sports venues, check available time slots, make bookings, and manage their booking history. Turf owners receive a separate dashboard to manage their turf information, slots, and customer bookings, while administrators manage the overall system through Django Admin.

## Live Demo

**[Open TurfPay Live](https://turfpay.onrender.com/)**

---

## Key Features

### Turf Discovery

- Explore available sports turfs in Latur
- Search by turf name or location
- Filter venues by sport and maximum price
- View turf details, facilities, pricing, and available slots
- Display real venue images for easier selection

### Booking Management

- Book available turf slots
- View personal booking history
- Cancel existing bookings
- Automatic slot availability updates
- Protection against duplicate logical bookings for the same turf and time slot

### Customer Accounts

- Customer registration and login
- Secure authentication using Django's built-in authentication system
- Separate customer booking area
- Password reset workflow supported by Django authentication

### Turf Owner Dashboard

- Separate owner login experience
- Manage owned turf information
- View and manage customer bookings
- Monitor slot availability
- Keep owner management separate from customer booking actions

### Administration

- Django Admin panel for system administration
- Manage users, turfs, sports, slots, and bookings
- Separate administrator role from customer and owner workflows

### User Interface

- Clean dark-green sports marketplace design
- Responsive layout for desktop and smaller screens
- Django Templates with HTML and CSS
- Lightweight Vanilla JavaScript where required

---

## Technology Stack

- **Programming Language:** Python 3.13
- **Backend Framework:** Django 6.1
- **Frontend:** HTML5, CSS3, Django Templates, Vanilla JavaScript
- **Local Database:** SQLite
- **Production Database:** PostgreSQL on Neon
- **Database Connectivity:** psycopg, dj-database-url
- **Image Handling:** Pillow
- **Static File Serving:** WhiteNoise
- **Production Server:** Gunicorn
- **Deployment Platform:** Render
- **Version Control:** Git and GitHub

---

## Project Structure

```text
TurfPay/
│
├── accounts/          # Registration and account-related logic
├── bookings/          # Booking, cancellation and booking history
├── config/            # Django settings and project configuration
├── core/              # Shared pages, templates and static assets
├── templates/         # Shared authentication templates
├── turfs/             # Turf, sport, slot and owner management
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

The project follows Django's app-based structure so each major responsibility remains separated and easy to maintain.

---

## Booking Workflow

```text
Customer
   │
   ▼
Explore Turfs
   │
   ▼
View Turf Details
   │
   ▼
Choose Available Slot
   │
   ▼
Confirm Booking
   │
   ▼
Booking Stored in Database
   │
   ├── Customer Booking History Updated
   │
   └── Owner Booking Dashboard Updated
```

The booking logic also checks the logical combination of turf, date, start time, and end time so the same time period cannot be confirmed twice.

---

## User Roles

### Customer

- Explore turfs
- View turf details and slots
- Book available slots
- Cancel bookings
- View personal booking history

### Turf Owner

- Access the owner dashboard
- Manage owned turf information
- View customer bookings
- Monitor turf slot availability

### Administrator

- Access Django Admin
- Manage users and application data
- Manage turf, sport, slot, and booking records

---

## Running the Application Locally

### Clone the Repository

```bash
git clone https://github.com/manav-jagtap/TurfPay.git
cd TurfPay
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## Production Deployment

The live version of TurfPay uses:

- **Render** for web application hosting
- **Gunicorn** as the production WSGI server
- **WhiteNoise** for static file serving
- **Neon PostgreSQL** as the production database
- **Environment variables** for production configuration and sensitive values

Production and local development use the same Django codebase, with database configuration selected through environment settings.

---

## Data and Security

- Production credentials are stored in environment variables
- Secret keys and database passwords are not committed to GitHub
- Django authentication is used for user login and password handling
- Booking constraints help prevent duplicate confirmed reservations
- Local development database files and environment files are excluded through `.gitignore`

---

## Use Cases

- Students and groups looking for available sports turfs
- Working professionals planning games with friends
- Turf owners who want a simple way to manage bookings
- Academic project demonstration for Django, databases, authentication, and deployment
- Portfolio demonstration of a complete full-stack web application

---

## Future Enhancements

- Online payment integration
- Customer ratings and reviews
- Offer and coupon management
- Tournament and event listings
- Notifications for booking confirmations and cancellations
- Expanded support for additional cities
- Advanced owner analytics and revenue reporting

---

## Project Status

TurfPay currently includes the complete customer booking flow, owner management flow, administrator management, PostgreSQL production integration, and live Render deployment.

**Live Application:** [https://turfpay.onrender.com/](https://turfpay.onrender.com/)

---

## Author

**Manav Jagtap**  
B.Sc. Computer Science

If you find the project useful, consider giving it a star on GitHub.
