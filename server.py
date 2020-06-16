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

@app.route('/order-pizza')
def show_order_pizza_form():
    return render_template('order-pizza-form.html')

@app.route('/order-pizza', methods=['POST'])
def handle_pizza_order_submission():
    topping1 = request.form['topping1']
    topping2 = request.form['topping2']
    pizza = f'{topping1} and {topping2}'

    return f'One pizza with {pizza} on the way!'

@app.route('/spam-or-ham')
def show_spam_or_ham():
    return render_template('spam-or-ham.html')

@app.route('/spam-or-ham', methods=['POST'])
def handle_spam_or_ham_submission():
    user_input = request.form['user_input']
    result = predict(user_input)
    return f'Your word {user_input} is a {result}'
