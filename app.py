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
	municities = pd.read_csv('data.csv')
	collected = {}
	for step, city in municities.iterrows():
		temp_obj = {}
		temp_obj['name'] = city['name']
		temp_obj['coords'] = city['coords']
		temp_obj['watervalue'] = city['watervalue']
		temp_obj['avg consump'] = city['avg consump']
		collected[city['name']] = temp_obj
	stringed_data = json.dumps(collected)
	return render_template('index.html', citydata = stringed_data)

@app.route('/api/get_foiler', methods=['POST'])
def get_foiler():
	municities = pd.read_json ('Amiel Stuff/municipalities.json')
	pass

@app.route('/api/updateanobj', methods=['POST'])
def update_anobj():

	municities = pd.read_csv('data.csv')
	collected = {}
	for step, city in municities.iterrows():
		temp_obj = {}
		temp_obj['name'] = city['name']
		temp_obj['coords'] = city['coords']
		temp_obj['watervalue'] = city['watervalue']
		temp_obj['avg consump'] = city['avg consump']
		collected[city['name']] = temp_obj
	name = request.form["name"]
	wat = request.form["waterlevel"]
	con = request.form["consumption"]
	collected[name]['watervalue'] = wat
	collected[name]['avg consump'] = con
	li = []
	for obj in collected:
		li.append(collected[obj])

	df = pd.DataFrame(li)
	df.to_csv('data.csv')
	return render_template('update.html')

@app.route('/updateinfo', methods=['GET', 'POST'])
def get_updateinfo():
	return render_template('update.html')


if __name__ == '__main__':

	
	app.run(debug=True)	