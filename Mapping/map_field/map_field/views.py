from map_field import app
from flask_caching import Cache
from flask import request
app.config['CACHE_TYPE']='simple'
app.cache=Cache(app)
import json
import io
from flask import jsonify

from map_field import worker



@app.route('/train/format/match',methods=['post'])
def map_field():
	try:
		req_json=request.json
		source=req_json["source"]
		target=req_json["target"]
		res=worker.MapingFields(source,target).Map_Fields('match')
		return jsonify(res)
	except:
		return "Error"

@app.route('/train/format/learn',methods=['post'])
def map_learn():
	
		
		req_json=request.json
		source=req_json["source"]
		target=req_json["target"]
		mappings=req_json["mappings"]
		res=worker.MapingFields(source,target).Map_Learn(mappings)
		return jsonify(res) 
	
@app.route('/format/match',methods=['post'])
def map_automation():
	try:
		req_json=request.json
		source=req_json["source"]
		target=req_json["target"]
		res=worker.MapingFields(source,target).Map_Fields('match1')
		return jsonify(res)
	except:
		return "Error"
