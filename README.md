# 🧹 Freshious Cleaning

A professional cleaning service website built with **Django** and **Bootstrap 5**.

## Pages

| URL | Description |
|-----|-------------|
| `/` | Home — hero, services overview, testimonials, CTA |
| `/services/` | Full service list with pricing and add-ons |
| `/about/` | Company story, mission/values, team |
| `/contact/` | Booking form and contact information |

## Tech Stack

- **Backend:** Django 6.x (Python 3.12)
- **Frontend:** Bootstrap 5.3, Bootstrap Icons, Google Fonts (Poppins)
- **Database:** SQLite (development)

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Freshious_cleaning
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate
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

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Project Structure

```
Freshious_cleaning/
├── freshious_cleaning/     # Django project settings & root URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                   # Main app
│   ├── views.py            # All page views
│   └── urls.py
├── templates/              # HTML templates
│   ├── base.html           # Shared layout (navbar + footer)
│   ├── home.html
│   ├── services.html
│   ├── about.html
│   └── contact.html
├── static/
│   ├── css/style.css       # Custom styles
│   ├── js/main.js          # Scroll effects & animations
│   └── images/             # Local images
├── requirements.txt
├── .gitignore
└── manage.py
```

## License

MIT
