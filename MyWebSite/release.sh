#!/usr/bin/env bash
rsync -avz --exclude venv --exclude .git --exclude .idea --exclude '*__pycache__*' \
--exclude '*.sqlite3' --exclude '*.ini' --exclude '*/.DS_Store' --exclude 'localhost.*' \
. bart-jetson:sites/bartheupers.nl/
