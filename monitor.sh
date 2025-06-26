#!/bin/bash
# Monitoring script for racer-login-app

APP_URL=${1:-http://127.0.0.1:5000/healthz}
LOG_FILE="monitor.log"

while true; do
    TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
    if curl -fsS "$APP_URL" | grep -q "OK"; then
        echo "$TIMESTAMP - App is healthy" | tee -a "$LOG_FILE"
    else
        echo "$TIMESTAMP - App is DOWN!" | tee -a "$LOG_FILE"
        echo "ALERT: App is DOWN!"
    fi
    sleep 30
done 