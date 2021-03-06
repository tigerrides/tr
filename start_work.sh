#!/bin/bash

# this script automates the initialization workflow 

# sync with github
echo ""
echo "pulling latest changes from github"
git pull
echo ""
echo "Displaying git status"
git status
echo ""
echo "Check your current branch!"
git branch

echo ""
echo "DO THIS MANUALLY: START VIRTUALENV ON YOUR OWN"
echo "Run the command 'source django_env/bin/activate'"

echo ""
echo "Are you running tigerride locally?"
if git branch | grep "* local"
then
  echo "Running locally (if this isn't what you want, stop this script, run 'pg_ctl -D ./postgres_local_db stop', change your branch, and restart this script"
  echo "Starting local postgres server"
  pg_ctl -D ./postgres_local_db -l logfile start
else
  echo "It looks like you aren't"
fi
