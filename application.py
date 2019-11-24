import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import re
import flask
import praw
from flask import Flask, render_template, request
from sklearn.externals import joblib


app=Flask(__name__)

@app.route('/')

@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/statistics')
def statistics():
    return flask.render_template('statistics.html')

@app.route("/register", methods=["POST"])
def register():
    if request.method=='POST':
        nm = request.form.get("url")
        mm=nm 
        phrase=nm       
        filename2='log_gun_model_trained3.sav'
        loaded_model2 = joblib.load(filename2)
        arg=loaded_model2.predict(([phrase]))
        from json.encoder import JSONEncoder
        final_entity = { "predicted_argument": [arg[0]]}
        # directly called encode method of JSON
        print (JSONEncoder().encode(final_entity))       
    return flask.render_template('result.html',prediction=arg[0],url=mm)
        
