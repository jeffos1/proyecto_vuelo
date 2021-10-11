from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/home/')
def index():
    return render_template("home.html")


@app.route('/search_results')
def search():
    return render_template("search_results.html")


@app.route('/login/')
def login():
    return render_template("login.html")


@app.route('/plantilla')
def plantilla():
    return render_template("plantilla.html")


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


@app.route('/dashboard_child')
def dashboard_child():
    return render_template("dashboard_child.html")


if __name__ == '__main__':
    app.run(debug=True)
