from urllib import request
from webbrowser import get
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

#GET, POST, PUT, PATCH, DELE, methods={} TE
@app.route('/post/<post_id>', methods=['GET' 'POST'])
def lala(post_id):
    if request.method == 'get':
        return 'el id del post es: ' + post_id
    else:
        return 'este es otro metodo y no get'


@app.route('/')
def lele():
    print(request.form)
    print(request.form['llave1'])
    print(request.form['llave2'])
    return 'lele'