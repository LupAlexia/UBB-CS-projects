from repo.repo_sentence import TextFileRepoSentence
from service.service_sentence import ServicesSentence
from ui.ui import ConsoleUI

sentence_repo = TextFileRepoSentence()
sentence_services = ServicesSentence(sentence_repo)
ui = ConsoleUI(sentence_services)
ui.read_input()
