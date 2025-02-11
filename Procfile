web: python manage.py collectstatic --noinput && gunicorn --workers 5 --worker-class gevent --bind 0.0.0.0:8080 myshop.wsgi:application

