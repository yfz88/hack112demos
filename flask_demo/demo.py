''' Flask Demo

Flask can be used to quickly develop and host web pages.
This code just loads a simple HTML page, located at templates/sample.html.
To run, type "py -m flask --app demo run" into your terminal.

You can also just run this file directly with "python demo.py"
provided you have the if __name__ == '__main__': block at the bottom.
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('sample.html')

if __name__ == '__main__':
  app.run(port=7777, debug=True)