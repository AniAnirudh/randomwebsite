"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    #"""Renders the home page."""
    return render_template('Home.html',title='Home Page',year=datetime.now().year,)

@app.route('/my-link/')
def my_link():
  print ('console: leads to nowhere!')
  return render_template('OnClick.html',title='OnClick Page',year=datetime.now().year,)
