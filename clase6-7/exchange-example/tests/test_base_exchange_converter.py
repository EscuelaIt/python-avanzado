import pytest

from exchange_escuela_it.bases.base_exchange_converter import BaseExchangeConverter


class TestExchangeConverter(BaseExchangeConverter):
    currency_code = "USD"

    def get_values_from_api(self):
        return 0


def test_fail_due_not_implement_method():

    with pytest.raises(TypeError):

        class FailExchangeConverter(BaseExchangeConverter):
            pass

        FailExchangeConverter()  # pylint: disable=abstract-class-instantiated


def test_base_representations():
    test_exchange_converter = TestExchangeConverter()
    assert str(test_exchange_converter) == "USD Converter"
    assert repr(test_exchange_converter) == "TestExchangeConverter(currency_code=\"USD\")"
    assert repr(test_exchange_converter) == f"{TestExchangeConverter.__name__}(currency_code=\"USD\")"
