web: python manage.py runserver
web: gunicorn --pythonpath /brainfood/seniorproject "seniorproject.wsgi:app" --log-file -
heroku ps:scale web=1