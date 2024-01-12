import unittest
from flask import Flask
from flask_testing import TestCase
from App import app, record_request

class TestStatisticsAPI(TestCase):
    """
    Test class for the Statistics API endpoints.

    This class contains unit tests for the /api/statistics endpoint
    in the Flask application. It includes tests for scenarios with
    both empty and non-empty request history.

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
    
    def test_get_statistics_empty_history(self):
        """
        Test the /api/statistics endpoint with an empty request history.

        This test checks if the endpoint returns a 404 status code
        and contains the expected error message when there is no history.
        """
        response = self.client.get('/api/statistics')
        if response is not None:
            print(response.data.decode('utf-8'))
            self.assertEqual(response.status_code, 404)
            self.assertIn('No statistics available', response.get_json()['error'])
        else:
            print("Response is None")
    
    def test_get_statistics_with_history(self):
        """
        Test the /api/statistics endpoint with non-empty request history.

        This test checks if the endpoint returns a 200 status code
        and contains the expected message when there is a request history.
        """
        record_request('generate_numbers', int1=2, int2=3, limit=10, str1='foo', str2='bar')
        response = self.client.get('/api/statistics')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Most used request', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()