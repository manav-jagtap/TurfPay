# TurfPay

TurfPay is a web-based turf discovery and booking platform built for sports players and turf owners in Latur. It allows customers to explore local turfs, check available slots and manage bookings, while turf owners can manage their venues and customer bookings from a separate dashboard.

## Project Overview

The project was created to solve a common local problem: players often have to contact multiple turf owners individually to find an available slot. TurfPay brings turf discovery, slot availability and booking management into one web application.

## Main Features

- Explore sports turfs available in Latur
- Search and filter turfs by sport, location and price
- View turf details, facilities and available slots
- Customer registration and login
- Turf booking and cancellation
- Double-booking protection for time slots
- Customer booking history
- Separate turf owner dashboard
- Owner-side turf and booking management
- Django admin panel for system administration
- Responsive web interface

## User Roles

### Customer
- Explore available turfs
- View turf details and slots
- Book available slots
- Cancel bookings
- View personal booking history

### Turf Owner
- Access the owner dashboard
- Manage owned turf information
- View and manage customer bookings
- Monitor slot availability

### Administrator
- Manage application data through Django Admin
- Manage users, turfs, sports, slots and bookings

## Technology Stack

| Area | Technology |
| --- | --- |
| Backend | Python, Django 6.1 |
| Frontend | HTML5, CSS3, Django Templates, Vanilla JavaScript |
| Local Database | SQLite |
| Production Database | PostgreSQL (Neon) |
| Database Driver | psycopg, dj-database-url |
| Static Files | WhiteNoise |
| Production Server | Gunicorn |
| Image Handling | Pillow |
| Deployment | Render |
| Version Control | Git, GitHub |

## Project Structure

```text
TurfPay/
├── accounts/          # Authentication and customer account logic
├── bookings/          # Booking and cancellation workflow
├── config/            # Django project configuration
├── core/              # Shared pages, templates and static assets
├── templates/         # Shared authentication templates
├── turfs/             # Turf, sport, slot and owner management
├── .gitignore
├── manage.py
└── requirements.txt
```

## Booking Flow

```text
Customer
   ↓
Explore Turfs
   ↓
View Turf Details
   ↓
Choose Available Slot
   ↓
Confirm Booking
   ↓
Booking Stored in Database
   ↓
Customer and Owner Dashboards Updated
```

The booking logic prevents the same logical turf slot from being confirmed more than once.

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/manav-jagtap/TurfPay.git
cd TurfPay
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Run the development server

```bash
python manage.py runserver
```

Open the local server in your browser at `http://127.0.0.1:8000/`.

## Production Setup

The deployed version uses:

- Render for application hosting
- Gunicorn as the production WSGI server
- WhiteNoise for static file serving
- Neon PostgreSQL for the production database
- Environment variables for production configuration

## Security and Configuration

Sensitive production values such as database credentials, secret keys and passwords are stored in environment variables and are not committed to the repository.

## Project Status

TurfPay currently includes the complete customer booking flow, owner management flow, admin management, production database integration and Render deployment.

## Author

**Manav Jagtap**  
B.Sc. Computer Science
