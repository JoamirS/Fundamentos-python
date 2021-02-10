class ExtratorArgumentoUrl:
    def __init__(self, url):
        if self.url_e_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!")

    def url_e_valida(self, url):
        if url:
            return True
        else:
            return False
