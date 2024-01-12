import unittest
from flask import Flask
import fetch_records  


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = fetch_records.app
        self.client = self.app.test_client()

    def test_user_id_returns_200(self):
        response = self.client.get('/api/v1/user/100000/karma-position')
        print("\n"+ str(response.status_code))
        self.assertEqual(response.status_code, 200)

    def test_print_output(self):
        response = self.client.get('/api/v1/user/3/karma-position')
        print(response.data)

if __name__ == '__main__':
    unittest.main()