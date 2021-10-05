from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index/')
@app.route('/home/')

def inicio():
    return '<ul><li><a href="/login">Login</a></li><li><a href="/recuperar">Recuperar datos</a></li></ul>'

if __name__=='__main__':
    app.run(debug=True)