from flask import Flask, render_template, request, redirect, url_for
from LIFX import LIFX

app = Flask(__name__)
lifx = LIFX()
@app.route('/', methods=["GET","POST"])
@app.route('/index', methods=["GET","POST"])
def index():
    return render_template('index.html', title='LIFX App', lifx_id="")

@app.route('/on', methods=["GET","POST"])
def on():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.power_on()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/off', methods=["GET","POST"])
def off():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.power_off()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/pulse', methods=["GET","POST"])
def pulse():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.pulse()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/mex', methods=["GET","POST"])
def mex():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.mex()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/mang', methods=["GET","POST"])
def mang():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.mang()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/pis', methods=["GET","POST"])
def pis():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.pis()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/hyg', methods=["GET","POST"])
def hyg():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.hyg()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/blu', methods=["GET","POST"])
def blu():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.blu()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/lad', methods=["GET","POST"])
def lad():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    print(lifx.token, type(lifx.token))
    lifx.lad()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/vda', methods=["GET","POST"])
def vda():
    message = request.form.get('lifx_id')
    print(type(message), message)
    lifx.token = message
    lifx.vda()
    return render_template('index.html', title='LIFX App', lifx_id=message)

@app.route('/hab', methods=["GET","POST"])
def hab():
    message = request.form.get('lifx_id')
    lifx.token = message
    lifx.hab()
    return render_template('index.html', title='LIFX App', lifx_id=message)

if __name__ == '__main__':
    app.run(debug=True)