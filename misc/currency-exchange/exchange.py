import collections
import requests
import json

COINBASE_PRO_API = "https://api.pro.coinbase.com/products/"

class Exchange:

    def __init__(self):
        self.exchange_rates = collections.defaultdict(dict)

    def get_list_of_base_quote(self):
        return json.load(requests.get(COINBASE_PRO_API).content)

    def parse_tickers(self):

        list_of_base_quotes = self.get_list_of_base_quote()

        for base_quote in  list_of_base_quotes:
            url = COINBASE_PRO_API + base_quote + "/ticker"
            data = json.load(requests.get(url).content)

            base, quote = base_quote.split('-')
            exchange_rate_base_to_quote = data["bid"]
            exchange_rate_quote_to_base = 1 / data["ask"]
            self.exchange_rates[base][quote] = exchange_rate_base_to_quote
            self.exchange_rates[quote][base] = exchange_rate_quote_to_base

    def find_best_exchange_rate(self, current_currency, new_currency, amount):

        visited = set()

        def dfs(past_currency, temp_currency, amount):

            highest_amount = 0

            if temp_currency == new_currency:
                return amount
            elif temp_currency not in self.exchange_rates:
                return highest_amount

            for currency in self.exchange_rates[temp_currency]:
                if (temp_currency, currency) in visited or currency == past_currency:
                    continue
                print(temp_currency, currency)
                visited.add((temp_currency, currency))
                new_exchange_rate = self.exchange_rates[temp_currency][currency]
                new_amount = dfs(temp_currency, currency, amount * new_exchange_rate)
                highest_amount = max(highest_amount, new_amount)

            return highest_amount

        return dfs(None, current_currency, amount)


if __name__ == "__main__":
    x = Exchange()

    print(x.find_best_exchange_rate("USD", "EUR", 100))