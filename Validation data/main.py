from cpf_and_cnpj import Document

test_cpf = "12354367996"
test_cnpj = "15436940000103"

document_cnpj = Document.create_document(test_cnpj)
document_cpf = Document.create_document(test_cpf)

print(document_cnpj)
print(document_cpf)
