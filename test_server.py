import unittest
from server import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.data, b"Hello, World!")

    def test_status(self):
        response = self.client.get('/status')
        self.assertEqual(response.data, b"Server is running")

if __name__ == '__main__':
    unittest.main()
