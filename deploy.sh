#!/bin/bash
docker-compose -f docker-compose.stage.yml up -d && docker-compose -f docker-compose.stage.yml exec app python manage.py collectstatic --noinput

