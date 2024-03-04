# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        word_splitted = list(self.word)
        list_to_return = []
        for item in words_list:
            item_splitted = list(item)
            if sorted(word_splitted) == sorted(item_splitted):
                list_to_return.append(item)
        return list_to_return