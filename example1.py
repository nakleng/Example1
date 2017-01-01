
max_number = 100
current_value = 0
numbers = []
pair = []

while max_number >= current_value:
    numbers.append(current_value)
    current_value += 1

for value in numbers:
    if value%2==0:
        pair.append(value)

print len(pair)
print len(numbers)