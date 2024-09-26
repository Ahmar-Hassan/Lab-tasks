def remove_punctuation(text):
    punctuation = ".,;!?:\"'()[]{}<>"
    result = ""

    for char in text:
        if char not in punctuation:
            result += char

    return result


user_input = input("Enter a Sentence: ")
print("Sentance without punctuation:", remove_punctuation(user_input))
