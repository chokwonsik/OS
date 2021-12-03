class Character:
    name = "John"
    age = 20
    weight = "40kg"
    __real_name = "Kim"
    __real_age = 30
    __real_weight = "60kg"

test = Character()
print(test.name)
print(test.age)
print(test.weight)
#print(test.__real_name)
print(dir(test))
print(test._Character__real_name)
print(test._Character__real_age)
print(test._Character__real_weight)