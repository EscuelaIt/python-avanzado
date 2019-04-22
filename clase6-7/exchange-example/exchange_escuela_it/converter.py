from .bases import USDCoverter, EURCoverter


class Converter:
    """
    Currency convertion

    Supported currencies ("USD", "EUR")

    .. note:

        Currency support depends on specific currency class implementation

    Usage:

    .. code-block:: python

        converter = Converter("USD")
        converter.convert_to_currency("EUR", 1000)
    """

    currency_converters = {
        "USD": USDCoverter,
        "EUR": EURCoverter,
    }

    def __init__(self, currency):
        self.currency = currency
        self.converter = self.currency_converters.get(currency)()

    def convert_to_currency(self, currency, amount):
        """
        Returns the amount converted in the selected currency

        :param currency: currency
        :type currency: str
        :param amount: current amount to convert
        :type amount: float
        :returns: convertion amount (float)
        """
        return self.converter.convert_to_currency(currency, amount)
