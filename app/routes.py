from flask import Flask, render_template             # From the flask module import the Flask class

app = Flask(__name__)               # Instantiate Flask into app (object)


@app.get("/")                       # Flask decorator that maps routes to view functions
def index():                        # A view function is a functio mapped to aroute (flask)
    me = {                          # A python dictionary containing keys and values.
        "first_name": "Alvin",
        "last_name": "Burgos",
        "hobbies": "Reading",
        "active": True
    }
    return me                       # A return statement (required)


@app.get("/about")
def about_me():
    return render_template("index.html")