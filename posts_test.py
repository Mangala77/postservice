
from posts import app

import os
import json
import unittest
import tempfile

class FlaskTestCase(unittest.TestCase):
    # Our first unit test - We are using the unittest
    # library, calling the posts route from the app
    # returned value, contained on the JSON response, match
    def test_posts(self):
        tester = app.test_client(self)
        response = tester.get('/api/v1.0/posts', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(json.loads(response.data), {"posts": 8})

if __name__ == '__main__':
    unittest.main()
