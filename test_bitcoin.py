import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):

#Mock the API call by providing a mock JSON response. 
# Assert that your program calculates the correct value in dollars.

    @patch('requests.get')
    def test_request_exchange_rate(self, mock_requests_get):
        
        example_api_response = {"time":{"updated":"Oct 10, 2020 01:37:00 UTC","updatedISO":"2020-10-10T01:37:00+00:00",
        "updateduk":"Oct 10, 2020 at 02:37 BST"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price "
        "Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","chartName":"Bitcoin",
        "bpi":{"USD":{"code":"USD","symbol":"&#36;","rate":"11,087.4885","description":"United States Dollar","rate_float":11087.4885},
        "GBP":{"code":"GBP","symbol":"&pound;","rate":"8,497.1407","description":"British Pound Sterling","rate_float":8497.1407},
        "EUR":{"code":"EUR","symbol":"&euro;","rate":"9,371.6775","description":"Euro","rate_float":9371.6775}}}
        mock_requests_get().json.return_value = example_api_response
        #dollars_exchange_rate = data['bpi']['USD']['rate_float']
        dollars_exchange_rate= bitcoin.get_exchange_rate(example_api_response)#the example response is the data
        converted = bitcoin.calculate_bitcoin_to_dollar(dollars_exchange_rate, 100 ) 
        expected = 11087.4885 * 100
        self.assertEqual(expected, converted)

        


#I did these to practice mocking input and printing
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