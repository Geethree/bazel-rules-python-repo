import unittest
from unittest.mock import Mock
import requests

# Mocking the requests.get method
def mock_get(*args, **kwargs):
    response = Mock()
    # You can customize the response here
    response.status_code = 200
    response.json.return_value = {"message": "Success"}
    return response

class TestHTTPRequest(unittest.TestCase):
    def setUp(self):
        # Patch the requests.get method with our mock_get
        self.get_patcher = unittest.mock.patch('requests.get', side_effect=mock_get)
        self.mock_get = self.get_patcher.start()

    def tearDown(self):
        # Stop the patching
        self.get_patcher.stop()

    def test_get_request(self):
        # Perform a get request (which is actually mocked)
        response = requests.get('https://example.com/api')

        # Assertions to check if the response is as expected
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Success"})
        self.mock_get.assert_called_once_with('https://example.com/api')

if __name__ == '__main__':
    unittest.main()
