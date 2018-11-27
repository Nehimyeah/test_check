import unittest, sys, json
from app import app
from flask_pymongo import PyMongo
from flask import Flask, request

class TestRestApi(unittest.TestCase):
	""" Ensure that the app starts correctly """

	def setUp(self):
		"""
		This method runs before each function is run and sets up necessary
		variables for the testing which is the self.tester here		
		"""
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
	"""
	Tests the get method for the restapi
	"""

	def setUp(self):
		self.app = app.test_client()
		

	def test_get_request(self):

		output = {
		    "result": []
		}
		response = self.app.get('/todo/api/tasks/v0.1')

		self.assertEqual(
			json.loads(response.get_data().decode(sys.getdefaultencoding())),
			output
			 )
if __name__ == '__main__':
	unittest.main()