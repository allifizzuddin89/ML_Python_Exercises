import unittest
import unittest_library

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = unittest_library.cap_text(text)
        self.assertEqual(result, 'Python')
    
    def test_multiple_word(self):
        text = 'monty python'
        result = unittest_library.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__=='__main__':
    unittest.main()

