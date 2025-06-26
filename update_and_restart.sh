#!/bin/bash
# Script to pull latest code and restart containers for racer-login-app

set -e

# Pull latest code
git pull origin main

# Build the latest Docker image
docker build -t mayur2808/racer-login-app:latest .

# Stop and remove any running container with the same name
docker rm -f racer-login-app || true

# Start the container
# (Adjust ports as needed)
docker run -d --name racer-login-app -p 5001:5000 mayur2808/racer-login-app:latest

echo "App updated and container restarted." 