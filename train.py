# <<<<<<< MITASK-O >>>>>>>
def calculateSumOfNumbers(arr):
    total = 0

    for item in arr:
        if type(item) in [int, float]:
            total += item

    return total


print(calculateSumOfNumbers([10, "10", {"son": 10}, True, 35]))

# <<<<<<< MITASK-N >>>>>>>
# def palindromeCheck(text):
#     return text == text[::-1]


# print(palindromeCheck("dad"))


# <<<<<<< MITASK-M >>>>>>>
# def getSquareNumbers(arr):
#     result = []

#     for num in arr:
#         result.append({
#             "number": num,
#             "square": num * num
#         })

#     return result


# print(getSquareNumbers([1, 2, 3]))
# <<<<<<< MITASK-L >>>>>>>
# def reverseSentence(text):
#     result = []

#     for word in text.split():
#         result.append(word[::-1])

#     return " ".join(result)


# print(reverseSentence("we like coding!"))
