class extractArgument:
    def __init__(self, url):
        if self.url_is_valid(url):
            self.url = url
        else:
            raise LookupError("URL inválida")

    @staticmethod
    def url_is_valid(url):
        if url:
            return True
        else:
            return False

    def extract_argument(self):

        search_source_currency = 'moedaorigem'
        search_destination_currency = 'moedadestino'

        initial_destiny_currency_index = self.url.find(search_destination_currency) + len(search_destination_currency) + 1

        origin_currency_initial_index = self.url.find(search_source_currency) + len(search_source_currency) + 1
        origin_currency_final_index = self.url.find("&")

        origin_currency = self.url[origin_currency_initial_index:origin_currency_final_index]
        destiny_currency = self.url[initial_destiny_currency_index:]

        return origin_currency, destiny_currency

    def find_initial_index(self, currency_sought):
        return self.url.find(currency_sought) + len(currency_sought) + 1
