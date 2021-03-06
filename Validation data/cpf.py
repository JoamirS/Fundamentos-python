class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.cpf_is_valid(document):
            self.cpf = document
        else:
            raise ValueError("CPF inválido")

    def __str__(self):
        return self.formated_cpf()

    def cpf_is_valid(self, document):
        if len(document) == 11:
            return True
        else:
            return False

    def formated_cpf(self):
        slice_from_first_third = self.cpf[:3]
        slice_from_fourth_sixth = self.cpf[3:6]
        slice_from_seventh_ninth = self.cpf[6:9]
        slice_from_tenth_eleventh = self.cpf[9:11]
        return (f"{slice_from_first_third}.{slice_from_fourth_sixth}.{slice_from_seventh_ninth}-{slice_from_tenth_eleventh} ")
