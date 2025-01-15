# testovani funkce is_teenager a get_upper_chards
# import unitest lib
import unittest

# import funkcii
from get_upper_chars import get_upper_chars
from is_teenager import is_teenager

# TestCase
class TestFunctions(unittest.TestCase):
    def test_is_teenager_19(self):
        result = is_teenager(19)
        self.assertEqual(result, True)

    def test_is_teenager_20(self):
        result = is_teenager(20)
        self.assertEqual(result, False)
    
    def test_is_teenager_10(self):
        result = is_teenager(10)
        self.assertEqual(result, False)

    def test_is_teenager_minus10(self):
        with self.assertRaises(ValueError):
            is_teenager(-10)

    def test_get_upper_chars_TJVB(self):
        result = get_upper_chars('Toto Je Veta Beta')
        self.assertEqual(result, 'TJVB')
    
    def test_get_upper_chards_TTSVKPSE(self):
        result = get_upper_chars('Toto je TeSt VelKych PiSmEn')
        self.assertEqual(result, 'TTSVKPSE')

# Run the tests
unittest.main()