web gunicorn thesisproject.wsgi:application --log-file -
web: python thesisproject/manage.py runserver 0.0.0.0:\$PORT
release: python thesisproject/manage.py makemigrations
release: python thesisproject/manage.py migrate