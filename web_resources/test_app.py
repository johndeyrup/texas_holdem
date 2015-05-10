'''
Created on May 10, 2015

@author: arilab
'''
import os
from flask import Flask, render_template
app = Flask(__name__)
print(os.listdir(app.template_folder))

@app.route('/')
def index():
    return 'Index Page TEst'

@app.route('/game_page')
def game_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)