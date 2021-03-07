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
        slice_from_first_third = self.cpf[:3]
        slice_from_fourth_sixth = self.cpf[3:6]
        slice_from_seventh_ninth = self.cpf[6:9]
        slice_from_tenth_eleventh = self.cpf[9:11]
        return (f"{slice_from_first_third}.{slice_from_fourth_sixth}.{slice_from_seventh_ninth}-{slice_from_tenth_eleventh} ")
