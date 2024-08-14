import unittest
from main import add, subtract, mult, div
import xmlrunner


class TestMain(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        
    def test_subtract(self):
        self.assertEqual(subtract(10,5), 5)
        
    def test_mult(self):
        self.assertEqual(mult(3, 4), 12)

    def test_div(self):
        self.assertEqual(div(8, 4), 2)

if __name__ == '__main__':
    # Create the directory if it does not exist
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')
    
    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))      
        