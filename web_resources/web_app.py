'''
Created on May 10, 2015

@author: arilab
'''
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='C:/Users/arilab/Documents/GitHub/web_app')


@app.route('/')
def hello_world():
    return 'Hi there'

@app.route('/welcome')
def welcomo():
    return 'meep'

@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for this user
    return 'User %s' % username

@app.route('/renderthings')
def render_page():
    return render_template('index.html')

def valid_login(username, password):
    user_passwords = {'bob':'hihi', 'sarah':'nike'}
    if user_passwords[username] == password:
        return True
    else:
        return False

@app.route('/login')
def login():
    if request.method == 'POST':
        return 'hi'
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'], request.form['password']):
#             return 'username'
#         else:
#             error = 'Invalid username/password'
# #     return render_Template('login.html', error = error)

if __name__ == '__main__':
    app.run(debug=True)