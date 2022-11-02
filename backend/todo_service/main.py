
from flask import Flask
from flask import jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
app.run(debug=True)
CORS(app)

# read file
with open('tasks.json', 'r') as myfile:
    data=myfile.read()


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return 'Get all taks!'

@app.route('/todo/create',methods=['POST'])
def createTask():
    req_data = request.get_json()
    obj.append(req_data)
    return jsonify(req_data)

@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    req_data = request.get_json()
    for idx, task in enumerate(obj):
        if task.get('task') == req_data["task"]:
            obj.pop(idx)
            obj.insert(idx,req_data)
            break
    return jsonify(req_data)

@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    req_data = request.get_json()
    for idx, task in enumerate(obj):
     if task.get('task') == req_data['task']:
        obj.pop(idx)
        return jsonify(req_data)
    return 'Item not Found'















#Para Rodar A Aplicação Flask.
#FLASK_APP=main.py flask run