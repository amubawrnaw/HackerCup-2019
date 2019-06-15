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


global anobj

@app.route('/', methods=['GET', 'POST'])
def start_app():
	municities = pd.read_csv('shit.csv')
	collected = {}
	for step, city in municities.iterrows():
		temp_obj = {}
		temp_obj['name'] = city['name']
		temp_obj['coords'] = city['coords']
		temp_obj['watervalue'] = city['watervalue']
		collected[city['name']] = temp_obj
	
	stringed_data = json.dumps(collected)
	return render_template('index.html', citydata = stringed_data)

@app.route('/api/get_foiler', methods=['POST'])
def get_foiler():
	municities = pd.read_json ('Amiel Stuff/municipalities.json')
	pass

@app.route('/api/updateanobj', methods=['POST'])
def update_anobj():
	name = request.args.get("name")
	pop = request.args.get("population")
	wat = request.args.get("waterval")
	con = request.args.get("consumption")
	anobj[name]['population'] = pop
	anobj[name]['waterval'] = wat
	anobj[name]['consumption'] con
	
@app.route('/api/get_geojson', methods = ['GET'])

if __name__ == '__main__':

	municities = pd.read_csv('shit.csv')
	collected = {}
	for step, city in municities.iterrows():
		temp_obj = {}
		temp_obj['name'] = city['name']
		temp_obj['coords'] = city['coords']
		temp_obj['watervalue'] = city['watervalue']
		collected[city['name']] = temp_obj
	
	anobj = collected
	app.run(debug=True)	