import unittest
from flask import Flask
from flask_testing import TestCase
from App import app, record_request

class TestGenerateNumbersAPI(TestCase):
    """
    Test class for the Generate Numbers API endpoints.

    This class contains unit tests for the /api/numbers endpoint
    in the Flask application. It includes tests for scenarios with
    both valid and invalid input parameters.

    Attributes:
    - app: Flask application instance for testing.
    - request_history: List to store request history for testing purposes.
    """
    
    def create_app(self):
        """
        Create a Flask application instance for testing.

        Returns:
        - Flask application instance.
        """
        app.config['TESTING'] = True
        return app
    
    def setUp(self):
        """
        Set up method to initialize testing environment.

        This method is executed before each test method.
        It resets the global request_history for testing purposes.
        """
        global request_history
        request_history = []
    
    def test_generate_numbers_valid_input(self):
        """
        Test the /api/numbers endpoint with valid input parameters.

        This test checks if the endpoint returns a 200 status code
        and if the response contains the expected content for valid input.
        """
        response = self.client.post('/api/numbers', data={
            'int1': 2,
            'int2': 3,
            'limit': 10,
            'str1': 'foo',
            'str2': 'bar'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('foo', response.get_json())

    def test_generate_numbers_invalid_input(self):
        """
        Test the /api/numbers endpoint with invalid input parameters.

        This test checks if the endpoint returns a 400 status code
        and if the response contains the expected error message for invalid input.
        """
        response = self.client.post('/api/numbers', data={
            'int1': 'invalid',
            'int2': 3,
            'limit': 10,
            'str1': 'foo',
            'str2': 'bar'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.get_json())

if __name__ == '__main__':
    unittest.main()