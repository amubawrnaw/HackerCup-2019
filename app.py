from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
from flask_uploads import UploadSet
from flask_uploads import configure_uploads
from flask_uploads import DATA
import os
import csv
import pandas as pd
import requests
import json
import math



app = Flask(__name__)
app.secret_key = __name__


@app.route('/', methods=['GET', 'POST'])
def start_app():
	return render_template('index.html')

@app.route('/api/get_foiler', methods=['POST'])
def get_foiler():
	
	pass

if __name__ == '__main__':
	app.run(debug=True)	