from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, Flask!'


# @app.route('/about')
# def about():
#     return 'This is the about page.'


@app.route('/user/<username>')
def hello(username):
    return f'Hello, {username.capitalize()}!'


# @app.route('/sum/<int:arg1>/<int:arg2>')
# def _sum(arg1, arg2):
#     return f'{arg1} + {arg2} = {arg1 + arg2}'


# @app.route('/files/<path:filepath>')
# def show_file(filepath):
#     return f'File located at: {filepath}'


# @app.route('/files/<path:filepath>/<int:arg1>')
# def show_file(filepath, arg1):
#     return f'path: {filepath}; num: {arg1}'


# @app.route('/user/<uuid:user_id>')
# def show_user_profile_by_uuid(user_id):
#     print(type(user_id))
#     return f'User with UUID: {user_id}'


if __name__ == '__main__':
    app.run(debug=True)
