# We can check if an element exists in the list by using 'in'

numbers = [1, 2, 3, 3]

print(4 in numbers)  # False
print(1 in numbers)  # True

# We can check what index location an element is at
print(numbers.index(2))  # 1

# We can see the total amount of times the value is present in a list
print(numbers.count(3))  # 2

# The 'count' logic can be blown to be the following


def count(items, target):
    result = 0
    for item in items:
        if item == target:
            result += 1
    return result


print(numbers.append(4))

print(numbers.insert(1, 5))

numbers = [1, 2, 3, 4, 5, 6]

numbers.pop()
print(numbers)  # [1, 2, 3, 4, 5]

numbers.pop(1)
print(numbers)  # [1, 3, 4, 5]
