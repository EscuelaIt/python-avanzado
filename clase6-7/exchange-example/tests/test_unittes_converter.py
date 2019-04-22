from unittest import TestCase, mock

from exchange_escuela_it.converter import Converter
from .utils import MockResponse


class ConverterCreation(TestCase):

    @mock.patch("requests.get")
    def test_call_converter(self, mock_request_get):
        mock_request_get.return_value = MockResponse({"base": "USD", "rates": {"EUR": 0.111}}, 200)
        conveter = Converter("USD")
        amount = conveter.convert_to_currency("EUR", 1000)
        assert amount == 111, amount
        self.assertEqual(amount, 111, amount)
        self.assertTrue(amount == 111, amount)
