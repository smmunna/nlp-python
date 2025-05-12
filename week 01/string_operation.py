text = "Hello there! Welcome to Python. Let's clean this text."

#Lower case
text = text.lower()

import string

text = text.translate(str.maketrans('','', string.punctuation))

#text split
word = text.split()

print(word)