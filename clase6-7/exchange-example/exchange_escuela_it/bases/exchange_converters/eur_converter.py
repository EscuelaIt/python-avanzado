import requests
import logging

from exchange_escuela_it.bases.base_exchange_converter import BaseExchangeConverter


logging.basicConfig(level=logging.DEBUG)


class EURCoverter(BaseExchangeConverter):
    currency_code = "EUR"
    url = f"https://api.exchangeratesapi.io/latest?base={currency_code}"

    def get_values_from_api(self):
        response = requests.get(self.url)
        logging.info(f'Getting response from {self.url} status_code:{response.status_code}')
        return response.json().get("rates")
