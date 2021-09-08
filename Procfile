release: python3.8 manage.py makemigrations --no-input
release: python3.8 manage.py migrate --no-input

web: gunicorn schMarket.wsgi