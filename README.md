# flask-app-ecs
Simple flask app to be run on ECS



# Language:
Your website is written in Python.

# Framework:
It uses Flask, a lightweight web framework for Python that's super popular for building simple web apps and APIs.

# Files you have:
app.py: This defines the main Flask application. 

You have two routes:
/ → returns a welcome message (with some HTML formatting, like <br>).
/health → returns a simple health check message (Server is up and running).

requirement.txt: 
It lists the Python packages needed — Flask and Werkzeug — so others can install them easily using pip install -r requirements.txt.
run.py: This is the script that actually runs your Flask app, making it listen on all IP addresses (0.0.0.0) on port 80.

# In short:
Language: Python
Framework: Flask
Type of website: A basic web server — probably a test app or a simple API endpoint, perfect for learning, demos, or small backend services.


# Code explanation of app.py
app = Flask(__name__)
This line creates your Flask web application.

🧱 Flask(...)
Flask is a class provided by the Flask framework.
When you write Flask(...), you're creating an object (like a machine) that can run a web server and handle routes (@app.route()).

🔤 __name__
__name__ is a special Python variable.
It holds the name of the current module (the current file name).
When you run your script directly, __name__ is set to "__main__".
Flask uses this to:
Know where your app's files are (like templates or static files)
Set the root path for your app

🔧 Putting it all together:
app = Flask(__name__)
This does:

✅ Creates an instance of a Flask app
✅ Registers your current Python file as the main web app
✅ Stores it in the variable called app

from flask import Flask

Line 1: Import the Flask class from the flask package.
* flask is the name of the installed package
* Flask is a class inside that package

requirement.txt will install this flask package.

pip install -r requirements.txt will install Flask
…if your requirements.txt file includes:

flask==2.2.2
Werkzeug==2.2.2
Then running:

pip install -r requirements.txt
will install:

Flask v2.2.2
Werkzeug v2.2.2 (Werkzeug is a Flask dependency)

###
def hello_world():
and
def health():

Above two are the functions which returns welcome message as an HTTP response.

Line 4-9: Define a route / (the root URL). When a user visits /, the function hello_world() runs and returns the welcome message as an HTTP response.
Line 11-14: Define another route /health. When a user visits /health, it returns the string 'Server is up and running'.

#run.py

from app import app
app.run(debug=True, host='0.0.0.0', port=80)

What this does:
> Line 1: Import the Flask app object named app from your app.py file.
> Line 2: Start the Flask development server with these options:
> debug=True: Enables debug mode (auto-reloads app on code changes + shows detailed error messages).
> host='0.0.0.0': Makes the server accessible from any IP address (not just localhost).
> port=80: Runs the server on port 80 (the default HTTP port).


What happens behind the scenes?
1. When you run the Flask app (app.run(...)), it starts a web server.
2. Whenever a client (browser, curl, etc.) sends an HTTP request to your app’s URL:
3. If the request URL path is / (the root), Flask matches it to the route decorated with @app.route('/').
4. Flask then calls the function hello_world() behind that route.
5. The function runs and returns the string response.
6. Flask sends that response string back to the client as the HTTP response.
7. Similarly, when the client visits /health, Flask calls your health() function automatically.
