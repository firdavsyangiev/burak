# <<<<<<< MITASK-M >>>>>>>
def getSquareNumbers(arr):
    result = []

    for num in arr:
        result.append({
            "number": num,
            "square": num * num
        })

    return result


print(getSquareNumbers([1, 2, 3]))
# <<<<<<< MITASK-L >>>>>>>
# def reverseSentence(text):
#     result = []

#     for word in text.split():
#         result.append(word[::-1])

#     return " ".join(result)


# print(reverseSentence("we like coding!"))
