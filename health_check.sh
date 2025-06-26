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