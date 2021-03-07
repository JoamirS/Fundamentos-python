from cpf_and_cnpj import CpfCnpj

test_cpf = "12354367996"
test_cnpj = "15436940000103"

document_cnpj = CpfCnpj(test_cnpj, 'cnpj')
document_cpf = CpfCnpj(test_cpf, "cpf")

print(document_cnpj)
print(document_cpf)
