#!/bin/sh

if [ "$1" = 'course_inspector' ]; then
    touch /var/log/cron.log
    echo "30 23 * * * /usr/local/bin/python3 /app/manage.py update_course_activities >> /var/log/cron.log 2>&1" > /etc/crontab
    crontab /etc/crontab
    cron && tail -f /var/log/cron.log

else
    echo "Waiting for postgres..."

    while ! nc -z "${POSTGRES_HOST}" "${POSTGRES_PORT}"; do
        sleep 0.1
    done
    echo "PostgreSQL started"

    echo "Migrate the Database at startup of project"
    python manage.py migrate --settings ${DJANGO_SETTINGS_MODULE} --noinput

    echo "Collect staticfiles at startup of project"
    python manage.py collectstatic --settings ${DJANGO_SETTINGS_MODULE} --noinput

    echo "Running gunicorn"
    gunicorn news.wsgi:application --bind 0.0.0.0:5000 --workers=3
fi
