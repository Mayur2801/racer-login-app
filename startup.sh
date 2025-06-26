#!/bin/bash
# Startup script for racer-login-app

cd "$(dirname "$0")/app"
source venv/bin/activate
python3 main.py &
APP_PID=$!

cd ..

# Wait for the app to become healthy
for i in {1..10}; do
    if bash health_check.sh; then
        echo "App started and healthy."
        exit 0
    fi
    sleep 2
done

echo "App failed to become healthy."
kill $APP_PID
exit 1 