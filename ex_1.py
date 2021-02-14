import random


first_list = [random.randint(-5, 5) for i in range(1, random.randint(5, 15))]
second_list = [random.randint(-5, 5) for y in range(1, random.randint(5, 15))]
my_list = set(first_list) - set(second_list)
print(my_list)
