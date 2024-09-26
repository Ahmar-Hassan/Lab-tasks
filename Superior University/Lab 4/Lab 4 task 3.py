def sort_words(words):
    sorted_list = []

    while words:
        smallest = words[0]
        for word in words:
            if word < smallest:
                smallest = word
        sorted_list.append(smallest)
        words.remove(smallest)

    return sorted_list

user_input = input("Enter words separated by spaces: ")
words = user_input.split()
sorted_words = sort_words(words)
print("Sorted words:", " ".join(sorted_words))
