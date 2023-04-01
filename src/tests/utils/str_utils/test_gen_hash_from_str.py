from django.test import TestCase

from src.utils.str_utils import gen_hash_from_str

class GenHashFromStrTest(TestCase):        
    def test_gen_hash_from_str_0(self):
        self.assertEqual(gen_hash_from_str('Q w E r T y 1@3$/\,.'), 'qwerty13')
    def test_gen_hash_from_str_1(self):
        self.assertEqual(gen_hash_from_str(1234), False)
    def test_gen_hash_from_str_2(self):
        self.assertEqual(gen_hash_from_str(-1234), False)
    def test_gen_hash_from_str_3(self):
        self.assertEqual(gen_hash_from_str(['qwerty', 1, 2, 3]), False)
    def test_gen_hash_from_str_4(self):
        self.assertEqual(gen_hash_from_str({'qwerty' : 123}), False)
    def test_gen_hash_from_str_5(self):
        self.assertEqual(gen_hash_from_str(''), False)
    def test_gen_hash_from_str_6(self):
        self.assertEqual(gen_hash_from_str(), False)