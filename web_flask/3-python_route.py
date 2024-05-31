#!/usr/bin/python3
"""Start a flask web app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return Hello HBNB"""
    return 'Hello HBNB'


@app.route('/hbnb')
def hbnb():
    """Return HBNB"""
    return 'HBNB'


@app.route('/C/<text>')
def c_is_fun(text):
    """Return 'C followed by the value of the text variable (replace underscore _ symbols with a space )"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )
The default value of text is “is cool”"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
