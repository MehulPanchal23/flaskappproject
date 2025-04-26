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
