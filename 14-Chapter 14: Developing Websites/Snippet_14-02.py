# Import Flask
from flask import Flask

# Create the app object
app = Flask(__name__)

# Define the hello function, with route decorator
@app.route("/")
def hello():
  return "<h1>Hello, World!</h1>"
