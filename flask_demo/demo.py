''' Flask Demo

Flask can be used to quickly develop and host web pages.
This code just loads a simple HTML page, located at templates/sample.html.

'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('sample.html')