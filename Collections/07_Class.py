test_one = []
test_two = ()
print(type(test_one))
print(type(test_two))

ages_list = [15, 87, 56, 65, 32, 89, 5]
for counter in range(len(ages_list)):
    print(counter, ages_list[counter])

for index, age in enumerate(ages_list):
    print(f"índice: {index} idade: {age}")

users_list = [
    ("Guilherme", 37, 1981), ("Joamir", 31, 1998), ("Paulo", 39, 1995)
             ]

for name, age, born in users_list:
    print(f"Nome: {name}")
