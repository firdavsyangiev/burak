def reverseSentence(text):
    result = []

    for word in text.split():
        result.append(word[::-1])

    return " ".join(result)


print(reverseSentence("we like coding!"))
