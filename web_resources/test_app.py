'''
Created on May 10, 2015

@author: arilab
'''
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

#Dictonary of users and passworkds
valid_pass = {'bob':'smith', 'sarah':'micheals'}

#Default login page see index.html, this should be changed to login.html once homepage is created
@app.route('/')
def Login():
    return render_template('index.html')

#Do something with the results from the form, the variables see index.html user and pass, these get
#stored in user and password. In the index.html login causes this method to be run
@app.route('/', methods=['POST'])
def check_password():
    user = request.form['user']
    password = request.form['pass']
    try:
        if valid_pass[user] == password:
            return redirect(url_for('game'))
        else:
            return 'Invalid username or password'
    except:
        return 'Invalid username or password'

#Renders gamescreen
@app.route('/game')
def game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)