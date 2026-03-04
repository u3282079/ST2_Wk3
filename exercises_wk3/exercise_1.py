list_comprehension = [x for x in range (1, 100)]
divisible_list = [x for x in list_comprehension if x % 5 == 0]

print(list_comprehension)
print(divisible_list)