users_data_science = {15, 23, 43, 56}
users_machine_learning = {13, 23, 56, 42}

all_students_who_studied = users_data_science | users_machine_learning
print(sorted(all_students_who_studied))

studied_ml_but_did_not_ds = users_data_science - users_machine_learning
print(studied_ml_but_did_not_ds)

who_am_not_the_two_courses = users_data_science ^ users_machine_learning
print(who_am_not_the_two_courses)
