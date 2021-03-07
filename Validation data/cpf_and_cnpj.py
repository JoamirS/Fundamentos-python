from validate_docbr import CPF, CNPJ


class CpfCnpj:
    def __init__(self, document, type_document):
        self.type_document = type_document
        document = str(document)

        if self.type_document == "cpf":
            if self.validate_cpf(document):
                self.cpf = document
            else:
                raise ValueError("CPF inválido")

        elif self.type_document == "cnpj":
            if self.validate_cnpj(document):
                self.cnpj = document
            else:
                raise ValueError("CNPJ inválido")
        else:
            raise ValueError("Documento inválido")

    def __str__(self):
        if self.type_document == "cpf":
            return self.format_cpf()
        elif self.type_document == "cnpj":
            return self.format_cnpj()

    def validate_cpf(self, cpf):
        if len(cpf) == 11:
            validator = CPF()
            return validator.validate(cpf)
        else:
            raise ValueError("Quantidade inválida de dígitos.")

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def validate_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos inválida.")

    def format_cnpj(self):
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)
