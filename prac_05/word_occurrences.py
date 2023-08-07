"""
Word Occurrences
Estimate: 30 minutes
Actual:   45 minutes
"""

text = input("Text: ")
words = text.split()

number_of_words = {}
for word in words:
    if word in number_of_words:
        number_of_words[word] += 1
    else:
        number_of_words[word] = 1

maximum_word_length = max(len(word) for word in number_of_words)

sorted_word = sorted(number_of_words.items())
for word, count in sorted_word:
    print(f"{word:>{maximum_word_length}} : {count}")
