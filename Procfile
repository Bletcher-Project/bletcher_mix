web: gunicorn bletcher_mix.wsgi:application --log-file - --log-level debug --timeout 180
python3 manage.py collectstatic --noinput
manage.py migrate