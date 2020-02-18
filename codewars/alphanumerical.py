"""Given a string, write a function that returns a string of numbers that represent the place of that letter in the alphabet"""
from string import ascii_lowercase
x = 1
letters = {}
for letter in ascii_lowercase:
    letters[letter] = x
    x += 1

text = "The sunset sets at twelve o' clock."
def alphabet_position(text):
    newtext = []
    text = text.lower()
    print(text)
    for letter in text:
        if letter in letters:
            letter = letters[letter]
            newtext.append(str(letter))
        else:
            pass
   
    return  ' '.join(newtext)

print(alphabet_position(text))