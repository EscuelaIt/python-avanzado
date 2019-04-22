import requests

from exchange_escuela_it.bases.base_exchange_converter import BaseExchangeConverter


class USDCoverter(BaseExchangeConverter):
    currency_code = "USD"
    url = f"https://api.exchangeratesapi.io/latest?base={currency_code}"

    def get_values_from_api(self):
        response = requests.get(self.url)
        return response.json().get("rates")
