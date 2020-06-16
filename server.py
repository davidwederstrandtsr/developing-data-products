from flask import Flask
from flask import render_template
from flask import request
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Ada')

@app.route('/another-page')
def another_page():
    return 'This is another web page'

# /users/profie/123
# /users/gocodeup
@app.route('/hello/<name>')
def sayhello(name):
    return f'Hello, {name}!'

# my-first-form application
@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting-result.html', greeting=greeting)


# spam-or-ham application
@app.route('/spam-or-ham')
def show_spam_or_ham():
    return render_template('spam-or-ham.html')

@app.route('/spam-or-ham', methods=['POST'])
def handle_spam_or_ham_submission():
    user_input = request.form['user_input']
    result = predict(user_input)
    return f'Your word {user_input} is a {result}'
