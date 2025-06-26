#!/bin/bash
# Set up local development environment for racer-login-app

set -e

cd "$(dirname "$0")/app"

# Check for python3
if ! command -v python3 &> /dev/null; then
    echo "python3 could not be found. Please install python3."
    exit 1
fi

# Check for venv module
if ! python3 -m venv --help &> /dev/null; then
    echo "The python3-venv package is not installed. Please run: sudo apt install python3-venv"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Ensure Flask and Flask-SQLAlchemy are installed
pip install Flask Flask-SQLAlchemy

# Initialize the database
export FLASK_APP=manage.py
flask db_init

echo "Development environment setup complete. To activate, run: source racer-login-app/app/venv/bin/activate" 

sudo apt install python3-venv 

#!/bin/bash
# Health check script for racer-login-app

APP_URL=${1:-http://127.0.0.1:5000/healthz}

if curl -fsS "$APP_URL" | grep -q "OK"; then
    echo "Health check passed."
    exit 0
else
    echo "Health check failed!"
    exit 1
fi

#!/bin/bash
# Startup script for racer-login-app

cd "$(dirname "$0")/app"
source venv/bin/activate
python3 main.py &
APP_PID=$!

# Wait for the app to become healthy
for i in {1..10}; do
    if bash ../health_check.sh; then
        echo "App started and healthy."
        exit 0
    fi
    sleep 2
done

echo "App failed to become healthy."
kill $APP_PID
exit 1 