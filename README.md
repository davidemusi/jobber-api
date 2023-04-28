<h1> Jobber-API</h1> 

<p>This is a RESTful API for a job site built with Django Rest Framework.</p>

This API is hosted on Heroku and can be accessed at the following URL:
https://jobsite-api.herokuapp.com/

<h3>Endpoints</h3> 

* https://jobsite-api.herokuapp.com/application/ - Allows CRUD operations on 
* https://jobsite-api.herokuapp.com/candidate/ - Allows CRUD operations on candidates
* https://jobsite-api.herokuapp.com/candidatelogin/ - Allows candidate login

<h3>Technologies</h3> 

* Python 3.11.3
* Django 4.2
* Django REST Framework 3.14.0


<h2>Getting Started</h2> 

1. Clone the repository: git clone https://github.com/davidemusi/jobber-api.git

2. Create a virtual environment: python -m venv env

3. Activate the virtual environment: env\Scripts\activate (Windows) or source env/bin/activate (macOS/Linux)

4. Install the dependencies: pip install -r requirements.txt

5. Run the migrations: python manage.py migrate

6. Start the development server: python manage.py runserver
Deployed API

<h2>License</h2> 
This project is licensed under the MIT License. See the LICENSE file for details.
