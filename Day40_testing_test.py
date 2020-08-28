import unittest
import Day40_testing_main

class TestMain(unittest.TestCase):
    def test_data_ideal(self):
        arg1=12
        arg2=12
        result=Day40_testing_main.divide(arg1,arg2)
        self.assertEqual(result,1)

    def test_divide_zero(self):
        arg1=12
        arg2=0
        result=Day40_testing_main.divide(arg1,arg2)
        self.assertTrue(isinstance(result,ZeroDivisionError))

    def test_type(self):
        arg1='sadasdsadasdas'
        arg2=12
        result=Day40_testing_main.divide(arg1,arg2)
        self.assertTrue(isinstance(result,ValueError))


unittest.main()
