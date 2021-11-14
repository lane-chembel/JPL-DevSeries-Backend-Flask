import sys
sys.path.append('.')
sys.path.append('..')


import unittest
import app
class FlaskTest(unittest.TestCase):

    # check response 200
    def test_index(self):
        tester = app.app.test_client(self)
        response = tester.get("/getSomeData")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()