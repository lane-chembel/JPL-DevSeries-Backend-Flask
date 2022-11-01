import sys

sys.path.append('.')
sys.path.append('..')

import unittest
from DataClass import DataClass


class DataClassTest(unittest.TestCase):
    # check that employee data contains important keys
    def test_loadJsoon(self):
        test_class = DataClass()
        simple_hello = test_class.loadJson(filename='./data/hello.json')
        file = test_class.fileData
        self.assertTrue(file)

    def test_loadFile(self):
        test_class = DataClass()
        simple_hello = test_class.getJsonFromFile(filename='./data/hello.json')
        self.assertIn('message', simple_hello.keys())

    def check_global_data(self):
        test_class = DataClass()
        global_data = test_class.globalData
        self.asser

    def test_loadFileBig(self):
        test_class = DataClass()
        complex_hello = test_class.getJsonFromFile(filename='./data/hello-lots.json')
        self.assertEqual(len(complex_hello), 5)

        if __name__ == "__main__":
            unittest.main()
