from domain.sentence import Sentence


class ServicesSentence:
    def __init__(self, repo):
        self._repo = repo

    def add_sentence(self, sentence):
        s = Sentence(sentence)
        try:
            self._repo.add_sentence(s)
        except ValueError as e:
            raise

    def get_all(self):
        return self._repo.get_all()
