set COMPOSE_CONVERT_WINDOWS_PATHS=1
docker-compose -p tornRouter up -d --build
pause
docker-compose -p tornRouter down