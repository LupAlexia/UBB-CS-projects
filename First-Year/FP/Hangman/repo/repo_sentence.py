import os

from domain.sentence import Sentence


class TextFileRepoSentence:
    def __init__(self):
        self._text_file = "sentences.txt"
        self._data = self.load_from_file(self._text_file)

    def add_sentence(self, s):
        if self.find_sentence(s) is not None:
            raise ValueError("This sentence already exists")

        self._data.append(s)
        self.save_to_file(self._text_file)

    def find_sentence(self, s):
        index = None
        try:
            index = self._data.index(s)
        except ValueError:  # index() method returns ValueError if nothing was found
            return None
        return index

    @staticmethod
    def load_from_file(textfile):
        """
        Loads the list from a text file
        :param textfile:
        :return:
        """
        try:
            if not os.path.exists(textfile):
                return []  # Return an empty list if the file doesn't exist

            with open(textfile, "r") as file:
                sentences = file.readlines()
                # Strip newline characters from each line
                return [Sentence(sentence.strip()) for sentence in sentences]
        except IOError:
            pass

    def save_to_file(self, textfile):
        """
        Saves the list to a text file
        :param textfile:
        :return:
        """
        try:
            file = open(textfile, "w")
            for sentence in self._data:
                file.write(str(sentence.sentence) + "\n")
            file.close()
        except IOError as e:
            print("Error: " + str(e))

    def get_all(self):
        return self._data