'''
    input_of_user = "usuario reclama que não modem nao liga"

    sliced_string = set(input_of_user.split())
'''


def slice_information(input_string):
    sliced_input = set(input_string.split())
    return sliced_input


def burnt_equipment(input_string):
    for chosen_word in input_string:
        if chosen_word == "nao" or chosen_word == "liga":
            return "Equipamento não liga."
        else:
            return "O.S fora do escopo desejado."


order_of_service_information = str(input("Qual é a informação da O.S? "))

sliced_string = slice_information(order_of_service_information)
search_result = burnt_equipment(sliced_string)
print(search_result)
