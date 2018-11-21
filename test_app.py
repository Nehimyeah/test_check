import unittest
from app import app
from flask_pymongo import PyMongo
import sys
import json
from flask import Flask

app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'

class TestRestApi(unittest.TestCase):
	""" Ensure that the app starts correctly """

	def setUp(self):
		self.tester = app.test_client()

	def test_if_app_starts_correctly(self):
		""" Test if the application starts and returns the right HTTP response code """
		response = self.tester.get('/todo/api/tasks/v0.1', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_when_page_doesnt_exist(self):
		""" Test if the when the request is a page that doesn't exist """
		response = self.tester.get("/todo", content_type='application/json')
		self.assertEqual(response.status_code, 404)


	def test_application_instance_of_flask(self):
		"""" checks if the application instantiated is the instance of Flask """
		self.assertIsInstance(app, Flask)

class Testget(unittest.TestCase):

	def setUp(self):
		self.app = app.test_client()
		# mongo = PyMongo(app)
		# todo = mongo.db.todo
		# todo.insert({'title':'Personal', 'task': 'Dress well carry yourselves', 'complete': False})
		

	def test_get_request(self):

		output = {'result': [{'complete': True,
              'task': 'Get together with friends',
              'title': 'Friends'},
             {'complete': False,
              'task': 'Stop being dysfunctional',
              'title': 'Family'},
             {'complete': False,
              'task': 'Finish your assignment on time',
              'title': 'School'}]}





		response = self.app.get('/todo/api/tasks/v0.1')

		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding())),
			output
			)

		# self.assertEqual(
		# 	json.loads(response.get_data().decode(sys.getdefaultencoding())),
		# 	output
		# 	)

	# def test_delete_request(self):
	# 	output = {'result': "success"}

	# 	response = self.app.delete('/todo/api/tasks/v0.1')
	# 	self.assertEqual(
	# 		json.loads(response.get_data().decode(sys.getdefaultencoding())))

	# def test_put_request(self):
	# 	output = {'result': ''}


if __name__ == '__main__':
	unittest.main()