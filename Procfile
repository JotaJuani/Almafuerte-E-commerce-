web: python manage.py collectstatic --noinput && gunicorn --workers 2 --bind 0.0.0.0:$PORT myshop.wsgi:application

