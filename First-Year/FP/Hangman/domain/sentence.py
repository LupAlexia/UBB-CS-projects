class Sentence():
    def __init__(self, sentence):
        self.__sentence = sentence

    @property
    def sentence(self):
        return self.__sentence

    @sentence.setter
    def sentence(self, sentence):
        self.__sentence = sentence

    def __str__(self):
        return "Hangman sentence: " + str(self.__sentence)
    def __eq__(self, s):
        return isinstance(s, Sentence) and self.sentence == s.sentence