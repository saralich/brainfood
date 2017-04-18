web: python manage.py runserver
web: gunicorn --pythonpath /brainfood/seniorproject "seniorproject.wsgiapp:wsgiapp" --log-file -
heroku ps:scale web=1