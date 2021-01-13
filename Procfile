web: gunicorn bletcher_mix.wsgi:application --log-file - --log-level debug --bind 0.0.0.0:8000
python3 manage.py collectstatic --noinput
manage.py migrate