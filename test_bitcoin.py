import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):

    #use mock input() to force it to return '123'
    @patch('builtins.input', side_effect=['123'])
    def test_get_number_of_bitcoin(self, mock_input):
        num_of_bitcoin = bitcoin.get_number_of_bitcoin()
        self.assertEqual(123, num_of_bitcoin)

    #verify that input rejected if non-numerical; last value should be accepted
    @patch('builtins.input', side_effect=['asdf', 'test', '12.3'])
    def test_get_number_of_bitcoin_validation(self, mock_input):
        num_of_bitcoin = bitcoin.get_number_of_bitcoin()  #call method
        self.assertEqual(12.3, num_of_bitcoin)

    # mock print function
    @patch('builtins.print')
    def test_display_result(self, mock_print):
        #action   ????do I need to make variables like num_of_bitcoin = 10?
        bitcoin.display_result(10, 1234.56) #call method with data provided in test
        #assert that the following string is the result when the function is called with the above input
        mock_print.assert_called_with('$ 1234.56 is the equivalent of 10 bitcoins')


    def test_calculate_bitcoin_to_dollar(self):
        #calculate value using method
        value = bitcoin.calculate_bitcoin_to_dollar(123, 10)
        expected_value = 1230
        self.assertEqual(value, expected_value)