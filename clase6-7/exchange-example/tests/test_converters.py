from unittest import mock

from exchange_escuela_it.bases.exchange_converters import USDCoverter
from .utils import MockResponse


def mock_get_ratio_to_currency(*args):
    return 1


@mock.patch("requests.get")
def test_usd_converter_creation(mock_request_get):
    mock_request_get.return_value = MockResponse({"base": "USD", "rates": {"EUR": 0.111}}, 200)
    usd_converter = USDCoverter()
    usd_converter.get_ratio_to_currency = mock_get_ratio_to_currency
    assert usd_converter.conversions is not None
    assert usd_converter.conversions.get("EUR") == 0.111
    assert usd_converter.convert_to_currency("EUR", 1000) == 1000
