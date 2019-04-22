import abc


class BaseExchangeConverter(metaclass=abc.ABCMeta):
    conversions = None
    base_url = "https://api.exchangeratesapi.io/latest"
    currency_code = None

    def __init__(self):
        self.conversions = self.get_values_from_api()

    def __str__(self):
        return f"{self.currency_code} Converter"

    def __repr__(self):
        return f"{self.__class__.__name__}(currency_code=\"{self.currency_code}\")"

    @abc.abstractmethod
    def get_values_from_api(self):
        pass

    def get_ratio_to_currency(self, currency):
        if currency in self.conversions:
            return self.conversions[currency]
        raise ValueError(f"{currency} is not supported")

    def convert_to_currency(self, currency, amount):
        ratio = self.get_ratio_to_currency(currency)
        return ratio * amount
