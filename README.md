# TurfPay — Turf Booking Platform

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.1-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-4169E1?style=flat-square&logo=postgresql&logoColor=white)](https://neon.com/)
[![Render](https://img.shields.io/badge/Deployed%20on-Render-46E3B7?style=flat-square&logo=render&logoColor=black)](https://turfpay.onrender.com/)

TurfPay is a Django turf-discovery and slot-booking platform for players, turf owners, and administrators in Latur.

[Open Live Demo](https://turfpay.onrender.com/)

## Engineering Highlights

- Customer and turf-owner workflows
- Search and filtering by location, sport, and price
- Slot booking, cancellation, and booking history
- Duplicate-booking protection
- PostgreSQL production database on Neon
- Render deployment with environment-based configuration

## Core Features

### Customers

- Register and sign in securely
- Explore turf details, facilities, pricing, and available slots
- Book available time slots
- Review and cancel eligible bookings

### Turf Owners

- Access a separate owner dashboard
- Manage owned turf information
- Monitor slots and customer bookings

### Administrators

- Manage users, turfs, sports, slots, and bookings through Django Admin

## Booking Workflow

1. A customer explores available turfs.
2. The customer selects a turf, date, and time slot.
3. TurfPay validates availability and prevents duplicate reservations.
4. The booking is stored and shown to both the customer and turf owner.
5. Eligible cancellations return the slot to availability.

## Technology Stack

- Python 3.13 and Django 6.1
- HTML, CSS, Django Templates, JavaScript
- SQLite for local development
- PostgreSQL on Neon for production
- Pillow, WhiteNoise, Gunicorn, and Render

## Project Structure

```text
TurfPay/
├── accounts/          # Registration and account workflows
├── bookings/          # Booking, cancellation, and history
├── config/            # Django project configuration
├── core/              # Shared pages and assets
├── templates/         # Shared authentication templates
├── turfs/             # Turf, sport, slot, and owner management
├── manage.py
├── requirements.txt
└── README.md
```

## Run Locally

```bash
git clone https://github.com/manav-jagtap/TurfPay.git
cd TurfPay
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Production Setup

The live version uses Render, Gunicorn, WhiteNoise, and Neon PostgreSQL. Production database settings and sensitive values are supplied through environment variables rather than source code.

## Security

- Django authentication and password handling
- Environment-based secrets and database credentials
- Duplicate confirmed-booking constraints
- `.env` and local database files excluded through `.gitignore`

## Planned Enhancements

- Online payments
- Ratings and reviews
- Offers and coupons
- Tournament listings
- Booking notifications
- Owner revenue analytics
- Support for additional cities

## Author

**Manav Jagtap** — B.Sc. Computer Science student
