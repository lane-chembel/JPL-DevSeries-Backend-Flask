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
    # check that employee data is formatted correctly 
    def test_data(self):
       tester = app.app.test_client(self)
       response = tester.get("/getEmployees")
       keys = response[0].keys()
       self.assertIn('name', keys)
       self.assertIn('level of effort', keys)

if __name__ == "__main__":
    unittest.main()