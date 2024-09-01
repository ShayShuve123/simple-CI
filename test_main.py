import unittest
from main import add, subtract, mult, div
import xmlrunner
import os

class TestMain(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        
    def test_mult(self):
        self.assertEqual(mult(3, 4), 12)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)

if __name__ == '__main__':
    # Use the current working directory (Jenkins workspace) for test reports
    output_dir = os.path.join(os.getcwd(), 'test-reports')

    # Create the directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Write the test results to an XML file within the Jenkins workspace
    with open(os.path.join(output_dir, 'results.xml'), 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)
