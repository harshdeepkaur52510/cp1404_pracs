"""
word_occurrences.py
"""
words = input("Text: ")
list_of_words = words.split()
word_count = {}
for word in list_of_words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
for key, value in word_count.items():
    print(key, ":", value)
