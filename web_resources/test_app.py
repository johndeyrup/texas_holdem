'''
Created on May 10, 2015

@author: arilab
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def Login():
    return render_template('index.html')

@app.route('/game')
def Game():
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)