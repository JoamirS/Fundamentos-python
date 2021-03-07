from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.validate_cpf(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formated_cpf()

    def validate_cpf(self, cpf):
        if len(cpf) == 11:
            validator = CPF()
            return validator.validate(cpf)
        else:
            raise ValueError("Quantidade inválida de dígitos.")

    def formated_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

