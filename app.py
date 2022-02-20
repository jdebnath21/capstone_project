# Importing required libraries

from flask import Flask, render_template, request, redirect, url_for
import warnings
import pandas as pd
warnings.filterwarnings('ignore')

# Import the model library
# import model

# Initialize Flask
app = Flask(__name__)

# Defining root path
@app.route('/')
def home():
    return  "Hello World"