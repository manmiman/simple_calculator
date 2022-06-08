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

**How to test or use the simple calculator**:

1. Simply type in the project's domain url and the calculator endpoint with query parameter: 'https://simple-calculator-aiman.herokuapp.com/calculators/v1/qcalculus?uery=[input]'

2. E.g. https://simple-calculator-aiman.herokuapp.com/calculators/v1/qcalculus?uery=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=

3. The calculator can also be tested by using API platform such as Postman