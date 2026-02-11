docker compose up -d --build

# make sure the postgres container is ready, then run migrations
sleep 5
docker compose exec api python manage.py makemigrations
docker compose exec api python manage.py migrate
