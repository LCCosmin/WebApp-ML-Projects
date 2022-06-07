# About

The scope of this project is to implement a simple WebApp that will contain an API for each of my ML Projects so that I can use all of them at the same time without too much of a hussle.

# Project Structure

## Subfolders

    - frontend: react modules for the frontend server
    - backend: django modules + ml modules for the backend server
    - backend.ml_models_class: module containing all ML projects

# Known Issues

    - When using any of the functions, it generates a new src link for the files, however the browser uses the variant from the cache, resulting in it not properly updating
    - Ugly design

# Setup

1. Download the repository: `git clone https://github.com/LCCosmin/WebApp-ML-Projects.git`

## Frontend

1. Make sure you have npm installed: `sudo apt install npm`
2. Go into the 'frontend' folder: `cd frontend`
3. Install node-modules: `npm install node-modules`
4. Start the React server: `npm start`

A window with the React Application will launch in your default browser.

## Backend

1. Create a new environment: `python3 -m venv <name_of_the_virtualenv>`
2. Activate the environment: `source <name_of_the_virtualenv>/bin/activate`
3. Install requirements.txt: `pip install -r requirements.txt`
4. Go in the backend folder: `cd backend`
5. Start running the Django server: `python3 manage.py runserver`