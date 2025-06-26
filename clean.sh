#!/bin/bash
# Clean logs, cache, and temp files for racer-login-app

set -e

# Remove *.log files
find . -type f -name "*.log" -exec rm -f {} +

# Remove __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove .pyc files
find . -type f -name "*.pyc" -exec rm -f {} +

# Remove temp files (e.g., *~, .DS_Store)
find . -type f \( -name "*~" -o -name ".DS_Store" \) -exec rm -f {} +

echo "Logs, cache, and temp files cleaned." 