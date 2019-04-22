from unittest import mock

from exchange_escuela_it import Converter
from .utils import MockResponse


@mock.patch("requests.get")
def test_call_converter(mock_request_get):
    mock_request_get.return_value = MockResponse({"base": "USD", "rates": {"EUR": 0.111}}, 200)
    conveter = Converter("USD")
    amount = conveter.convert_to_currency("EUR", 1000)
    assert amount == 111, amount
