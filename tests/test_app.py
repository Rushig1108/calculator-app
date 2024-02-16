# tests/test_app.py

import unittest
from app import app

class TestCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Simple Calculator</h1>', response.data)

    def test_addition(self):
        response = self.app.post('/calculate', data=dict(
            num1=5,
            num2=3,
            operation='add'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>The result is: 8.0</p>', response.data)

    def test_subtraction(self):
        response = self.app.post('/calculate', data=dict(
            num1=5,
            num2=3,
            operation='subtract'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>The result is: 2.0</p>', response.data)

    def test_multiplication(self):
        response = self.app.post('/calculate', data=dict(
            num1=5,
            num2=3,
            operation='multiply'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>The result is: 15.0</p>', response.data)

    def test_division(self):
        response = self.app.post('/calculate', data=dict(
            num1=6,
            num2=3,
            operation='divide'
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>The result is: 2.0</p>', response.data)

if __name__ == '__main__':
    unittest.main()

