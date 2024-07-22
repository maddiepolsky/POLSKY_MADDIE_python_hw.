#Write a function that accepts a sentence and returns the number of letters and digits.

def count_things(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return letters, digits

sentence = "hi i just turned 16"

letters, digits = count_things(sentence)

print (f"Letters: {letters}, Digits: {digits}")

        