# <<<<<<< MITASK-W >>>>>>>
def chunkArray(arr, size):
    result = []

    for i in range(0, len(arr), size):
        result.append(arr[i:i + size])

    return result


print(chunkArray([1, 2, 3, 4, 5], 2))

# <<<<<<< MITASK-V >>>>>>>
# def countChars(text):
#     result = {}

#     for char in text:
#         result[char] = text.count(char)

#     return result


# print(countChars("hello"))

# <<<<<<< MITASK-T >>>>>>>
# def mergeSortedArrays(arr1, arr2):
#     return sorted(arr1 + arr2)


# print(mergeSortedArrays([0, 3, 4], [4, 6]))

# <<<<<<< MITASK-S >>>>>>>
# def missingNumber(numb):
#     n = len(numb)
#     return n * (n + 1) // 2 - sum(numb)


# print(missingNumber([3, 0, 1]))


# <<<<<<< MITASK-R >>>>>>>
# def calculate(calc):
#     a, sign, b = calc.split()

#     a = int(a)
#     b = int(b)

#     if sign == "+":
#         return a + b
#     elif sign == "-":
#         return a - b
#     elif sign == "*":
#         return a * b
#     elif sign == "/":
#         return a / b


# print(calculate("1 + 3"))


# <<<<<<< MITASK-Q >>>>>>>
# def hasProperty(obj, prop):
#     return prop in obj


# print(hasProperty({"name": "BMW"}, "name"))


# <<<<<<< MITASK-P >>>>>>>
# def objectToArray(obj):
#     return list(obj.items())


# print(objectToArray({"a": 10, "b": 20}))


# <<<<<<< MITASK-O >>>>>>>
# def calculateSumOfNumbers(arr):
#     total = 0

#     for item in arr:
#         if type(item) in [int, float]:
#             total += item

#     return total


# print(calculateSumOfNumbers([10, "10", {"son": 10}, True, 35]))

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
