web: sh -c 'cd backend && python manage.py collectstatic --no-input && gunicorn config.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 2'
