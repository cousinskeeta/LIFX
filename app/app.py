from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome')
    
if __name__ == '__main__':
    app.run(debug=True)