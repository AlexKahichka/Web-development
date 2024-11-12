from flask import Flask

app = Flask(__name__)


@app.route('/')
def homepage():
	return 'Hello , Flask!!!'


@app.route('/profile')
def profile():
	return 'This is your profile page'


@app.route('/login')
def login():
	return 'Welcome'


@app.route('/profile/<user_>')
def greetings(user_):
	return f'Hello, {user_}!'

@app.route('/numbers/<int:user_number>')
def age(user_number):
	return f'Your age will be {user_number + 1}'

@app.route('/names/<string:name>')
def welcome(name):
	return name.upper()


# @app.route('/names/<path:name>')
# def welcome(name):
#     return name
@app.route('/user/<uuid:user_id>')
def id_checker(user_id):
	return f'User with UUID:\n {user_id}'


if __name__ == '__main__':
	app.run(debug=True)
