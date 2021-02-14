import random


main_list = [random.randint(0, 1) for i in range(5, 15)]
main_list = [i for i in main_list if i != 0]
print(main_list)