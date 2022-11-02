from flask import Flask
from flask import jsonify
import json

app = Flask(__name__)
app.run(debug=True)

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
    return 'Create new task'
@app.route('/todo/update',methods=['UPDATE'])
def updateTask():
    return 'Update Task'
@app.route('/todo/delete',methods=['DELETE'])
def deleteTask():
    return 'Delete task'
















#Para Rodar A Aplicação Flask.
#FLASK_APP=main.py flask run