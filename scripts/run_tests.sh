#!/bin/sh

set -o errexit

cp .env.dev .env
coverage run --source='.' manage.py test
coverage html