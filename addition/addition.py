def addNumbers(num1, num2):
    sum = int(num1) + int(num2)
    print("The sum of", num1, "and", num2, "is", sum)
    return sum


def main():
    while True:
        try:
            input1 = int(input("Enter the first number: "))
            input2 = int(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    addNumbers(input1, input2)


main()
