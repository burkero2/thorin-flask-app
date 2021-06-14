import os
from flask import Flask, render_template

# Create an instance of the Flask class store in variabble app, 1st instance is the name of  the application's module
app = Flask(__name__)

# decorator routes to the lowest layer
@app.route("/")
def index():
    # return "<h1>Hello, World!</h1>"
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/careers")
def careers():
    return render_template("careers.html")

    
# __main__ is the name of the default module in Python
if __name__ == "__main__":
    app.run(
        host= os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT","5000")),
        debug = True) 
        # Must change this to debug = False when running final code