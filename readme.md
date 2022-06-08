**Simple Calculator**

This is a simple calculator project that is implemented through a web API.

The service offers an endpoint that reads a string input (in base64 encoding) and parses it.
It returns standard HTTP code and solution to the calculation in JSON form. If any error occurs, it will return standard HTTP code and general error message.

An example calculus query:

Original query: 2 * (23/(3*3))- 23 * (2*3)

With encoding: MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=

The specific endpoint is: 'https://simple-calculator-aiman.herokuapp.com/calculators/v1/qcalculus?uery=[input]'

Input is a base64 encoded query.

Return:

On success: JSON response of format: { "error": false, "result": number }

On error: { "error": true, "message": string }

**Steps to run on local dev env**:
- This project is built using python and django
- Requirements: Python, Pipenv

1. Clone repo on local dev machine
2. Run 'pipenv install -r requirements.txt' to install required dependencies/packages
3. Run 'pipenv shell' in project folder to activate virtual env
4. Run 'python manage.py makemigrations' and 'python manage.py migrate' to migrate database
5. Run 'python manage.py runserver' to deploy project to local server

**Process to deploy project to heroku:**

1. Create Procfile and add this line: web: 'gunicorn simple_calculator.wsgi --log-file -'

2. Create runtime.txt which contain the python version of this project (Python 3.6)

3. Install required packages to deploy django project: 'pipenv install gunicorn dj-database-url whitenoise psycopg2-binary python-decouple'

4. Add all packages to requirements.txt file: 'pip freeze > requirements.txt'

5. Add whitenoise, database, static files and variables configurations to settings.py

6. Login to heroku account / signup for heroku account

7. Create heroku app: 'heroku create simple-calculator-aiman'

8. Add Postgres add-on to heroku app: 'heroku addons:create heroku-postgresql:hobby-dev --app simple-calculator-aiman'

9. Add config vars in heroku dashboard of the app (specifically for secret key and allowed hosts)

10. Disable collectstatic: 'heroku config:set DISABLE_COLLECTSTATIC=1'

11. Push project to heroku: 'git push heroku master'

12. Migrate database: 'heroku run python manage.py migrate'

**How to test or use the simple calculator on heroku**:

1. Simply type in the project's domain url and the calculator endpoint with query parameter: 'https://simple-calculator-aiman.herokuapp.com/calculators/v1/qcalculus?uery=[input]'

2. E.g. https://simple-calculator-aiman.herokuapp.com/calculators/v1/qcalculus?uery=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=

3. The calculator can also be tested by using API platform such as Postman
