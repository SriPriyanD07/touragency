# Asia Tours Agency

A Django-based web application for managing and booking Asian tours. This platform allows users to browse various tour packages, view details, and make bookings.

## Features

- Browse tour packages by categories (Luxury, Economic, etc.)
- Detailed tour information and pricing
- User authentication (login/register)
- Contact form for inquiries
- Responsive design for all devices

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual Environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SriPriyanD07/touragency.git
   cd touragency
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root and add:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (optional, for admin access)
   ```bash
   python manage.py createsuperuser
   ```

7. **Load sample data** (optional)
   ```bash
   python manage.py load_luxury_tours
   python manage.py load_economic_tours
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure

```
worldtour/
├── asiantoursagency/       # Main app
│   ├── migrations/         # Database migrations
│   ├── static/             # Static files (CSS, JS, images)
│   ├── templates/          # HTML templates
│   ├── management/         # Custom management commands
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # App config
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── urls.py            # App URL routing
│   └── views.py           # View functions
├── worldtour/             # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py        # Project settings
│   ├── urls.py           # Main URL routing
│   └── wsgi.py
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Available Commands

- `python manage.py runserver` - Start the development server
- `python manage.py makemigrations` - Create new migrations
- `python manage.py migrate` - Apply database migrations
- `python manage.py createsuperuser` - Create admin user
- `python manage.py load_luxury_tours` - Load luxury tour data
- `python manage.py load_economic_tours` - Load economic tour data

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [@your_twitter](https://twitter.com/your_handle) - your.email@example.com
