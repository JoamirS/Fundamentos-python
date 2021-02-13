class ExtratorArgumentos:
    def __init__(self, url):
        if self.url_e_valida(url):
            self.url = url
        else:
            raise LookupError("Url Inválida!")

    @staticmethod
    def url_e_valida(url):
        if url:
            return True
        else:
            return False

    def extrair_argumentos(self):
        indice_inicial_moeda_destino = self.url.find("=", 15)

        indice_final_moeda_origem = self.url.find("&")
        indice_inicial_moeda_origem = self.url.find("=")

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:]

        return moeda_destino, moeda_origem