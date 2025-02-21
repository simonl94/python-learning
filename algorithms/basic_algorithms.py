def count_even(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_simplified(numbers):
    return sum(x % 2 == 0 for x in numbers)


print(count_even_simplified([1, 2, 3]))
print(count_even_simplified([2, 2, 2, 2, 2]))
print(count_even_simplified([5, 4, 1, 7, 9, 6]))

## Let's define 3 algorithms that do the same thing in different ways

## Version 1
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))
        return result
    
## Version 2    
def max_diff_two(numbers):
    ## The 'sorted' function here sorts the list.
    numbers = sorted(numbers)
    ## We can reference -1 being the largest number and is at the end, while 0 is the opposite and is the smallest number at the start
    ## So my subtracting the max from the min we can find the difference
    return numbers[-1] - numbers[0]

## Version 3    

## Intsead of using the sorted function, we simply call the 'max' and 'min' functions
def max_diff_three(numbers):
    return max(numbers) - min(numbers)