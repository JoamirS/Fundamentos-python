from validate_docbr import CPF, CNPJ


class Document:
    @staticmethod
    def create_document(document):
        if len(document) == 11:
            return DocumentCpf(document)
        elif len(document) == 14:
            return DocumentCnpj(document)
        else:
            raise ValueError("Quantidade de dígitos está incorreta")


class DocumentCpf:
    def __init__(self, document):
        if self.validate_cpf(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.format_cpf()

    def validate_cpf(self, document):
        validator = CPF()
        return validator.validate(document)

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)


class DocumentCnpj:
    def __int__(self, document):
        if self.validate_cnpj(document):
            self.cnpj = document
        else:
            raise ValueError("CNPJ inválido")

    def __str__(self):
        return self.format_cnpj()

    def validate_cnpj(self, document):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(document)

    def format_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)
