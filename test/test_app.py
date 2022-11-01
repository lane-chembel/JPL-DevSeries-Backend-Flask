import sys

sys.path.append('.')
sys.path.append('..')

import unittest
import app


# check response 200 from each
class FlaskTest(unittest.TestCase):

    def test_get_some_data(self):
        tester = app.app.test_client(self)
        response = tester.get("/getSomeData")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def from_file(self):
        tester = app.app.test_client(self)
        response = tester.get("/getSomeDataFromFile")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_get_employees(self):
        tester= app.app.test_client(self)
        response = tester.get("/getEmployees")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()
