from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/ross")
def ross():
    return "<p> Hi I'm Ross. </p><img src='https://bigelow.cc/wp-content/uploads/sites/3/cropped-ross-bigelow.png'> "

myData = {
        "name" : 'Ross Bigelow',
        "dream" : "To inspire others to fulfil thier dreams.",
        'age': 1,
        'birthdate': "2020-01-01"
    }

@app.route("/json")
def myJson():
    return myData

from flask import render_template

@app.route("/webpage")
def webpage():
    return render_template('hello.html')