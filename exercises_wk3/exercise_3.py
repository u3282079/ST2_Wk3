import math

numbers = {x: math.factorial(x) for x in range (1, 11)}

print(numbers)

result = numbers[6] * numbers[5]
print(result)