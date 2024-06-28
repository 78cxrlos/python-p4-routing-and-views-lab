#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return f'<p>{parameter}</p>'

@app.route('/count/<int:parameter>')
def count(parameter):
    return '<br>'.join(str(i) for i in range(parameter + 1))

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            result = 'Error: Division by zero'
    else:
        result = 'Error: Invalid operation'
    return f'<p>{num1} {operation} {num2} = {result}</p>'

if __name__ == '__main__':
    app.run(debug=True)