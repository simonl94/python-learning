from typing import List

# Declare array
number_list = [1, 10, 400, 99, 65, 7, 4, 2, 8, 321, 866]
print("Number list is: ", number_list)


def filter_small_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < 10]


# Re-assign the variable with the returned value from the function
number_list = filter_small_numbers(number_list)
print("Filtered list with no number exceeding 10: ", number_list)
