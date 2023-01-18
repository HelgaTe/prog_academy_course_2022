"""
Task: 1. Create a class that performs statistical processing of a text file - counting characters, words, sentences, etc.
Determine the required attributes-data and attributes-methods in class for working with the text file.
"""

class TextStat:
    def __init__(self, file):
        self.file = file

    def open_file(self):
        f = open(self.file)
        x = f.read()
        return x








f = TextStat('test.txt')
x = f.open_file()
print(len(x))