from flask import Flask, render_template
#from flask_wtf import FlaskForm
#from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    return render_template('home.html')

@app.route('/overOns', methods=['GET', 'POST'])
def overOns():
    return render_template('overOns.html')

@app.route('/tarieven', methods=['GET', 'POST'])
def tarieven():
    return render_template('tarieven.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')