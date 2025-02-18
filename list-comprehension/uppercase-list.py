# Declare the list variable
wordList = ["ken", "mark", "david", "john", "steve"]


def uppercaseList(wordList):
    print("Uppercasing all names....")
    return [element.upper() for element in wordList]


# Re-assign the variable with the returned value from the function
wordList = uppercaseList(wordList)
print("Uppercased list: ", wordList)
