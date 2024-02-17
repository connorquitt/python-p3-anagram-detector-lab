class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list):
        return[item for item in list if sorted(item) == sorted(self.word)]
