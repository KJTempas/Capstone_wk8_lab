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

    