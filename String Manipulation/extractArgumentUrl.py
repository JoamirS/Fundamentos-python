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
        initial_destiny_currency_index = self.url.find("=", 15) + 1

        origin_currency_initial_index = self.url.find("=") + 1
        origin_currency_final_index = self.url.find("&")

        origin_currency = self.url[origin_currency_initial_index:origin_currency_final_index]
        destiny_currency = self.url[initial_destiny_currency_index:]

        return origin_currency, destiny_currency

