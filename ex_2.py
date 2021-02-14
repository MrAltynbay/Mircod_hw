import random

main_list = [random.randint(0, 1) for i in range(5, 15)]
print(main_list)
main_list = [i for i in main_list if i != 0]
print(main_list)