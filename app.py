from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_pymongo import MongoClient
import os

app = Flask(__name__)
# 
client = MongoClient('mongodb://datastore:27017/todo')
api = Api(app)

db = client.todo

class Todo(Resource):
	""" Resource handler for get and post request """

	def get(self):
		""" get all the todos in the db """
		todo = db.todo

		output = []
		for t in todo.find():
			output.append({'title': t['title'], 'task': t['task'], 'complete': t['complete']})

		return jsonify({'result': output})

	def post(self):
		""" post request for adding new todo to the db """
		todo = db.todo

		title = request.json['title']
		task = request.json['task']
		complete = request.json['complete']

		new_todo_id = todo.insert({'title': title, 'task': task, 'complete': complete})

		t = todo.find_one({'_id': new_todo_id})
		if t: # checks if dictionary of a todo item is returned
			output = {'title': t['title'], 'task': t['task'], 'complete': t['complete']}
		else:
			output = 'didnt make new insertion'
		return jsonify({'result': output})
		
class TodoManipulate(Resource):

	def get(self, title):
		""" get a single todo appended to the url """
		todo = db.todo

		t = todo.find_one({'title': title})
		if t:
			output = {'title': t['title'], 'task': t['task'], 'complete': t['complete']}
		else:
			output = 'no result found'
		return jsonify({'result': output})

	def put(self, title):
		""" update a document when the task is completed """
		todo = db.todo

		t = todo.find_one({'title': title})
		if t:
			todo.update(
				{'_id': t['_id']},
				{'$set': {'complete': True}}
				)
			output = 'success'

		else:
			output = 'failure'
		return jsonify({'result': output})

	def delete(self, title):
		""" Deletes the todo appended to the url """
		todo = db.todo
		t = todo.find_one({'title': title})
		if t:
			todo.remove({'title': title})
			output = 'success'
		else:
			output = 'failure'

		return jsonify({'result': output})

api.add_resource(Todo, '/todo/api/tasks/v0.1')
api.add_resource(TodoManipulate, '/todo/api/tasks/v0.1/<title>')

if __name__=='__main__':
	app.run(host='0.0.0.0', debug=True)