from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Ivan Shepetko TI-92'
@app.route('/fisrt')
def first():
    num0 = None
    num1 = 124
    num2 = 123
    name = request.args.get("name", "World")
    return f'{num0}, {num2}, {num2}'



if __name__ == '__main__':
	app.run('0.0.0.0')

