import random


class ConsoleUI:
    def __init__(self, sentence_service):
        self._sentence_service = sentence_service

    def print_menu(self):
        print("This is the menu. The following functionalities are provided:\n"
              "1 - Add sentence.\n"
              "2 - Play game\n")

    def read_input(self):
        while True:
            self.print_menu()
            print("Your choice: ")
            choice = int(input("> "))

            if choice == 1:
                s = input("sentence: ")

                try:
                    words = s.split()
                    if len(words) < 1:
                        raise ValueError("Sentence must have at least one word")
                    for word in words:
                        if len(word) < 3:
                            raise ValueError("Words must have at least three characters")
                    self._sentence_service.add_sentence(s)
                except ValueError as e:
                    print(e)
            elif choice == 2:
                sentences = self._sentence_service.get_all()
                sentence1 = random.choice(sentences)
                sentence = sentence1.sentence.lower()

                revealed_sentence = self.print_sentence_hangman(sentence)
                guessed_letters = set()
                hangman_progress = ""
                max_mistakes = 7

                while hangman_progress != "HANGMAN":
                    print("Current sentence:", revealed_sentence)
                    print("Hangman progress:", hangman_progress)

                    guess = input("Guess a letter: ").lower()

                    if not guess.isalpha() or len(guess) != 1:
                        print("Please enter a single valid letter.")
                        continue

                    if guess in guessed_letters:
                        print(f"You already guessed '{guess}'. Try a new letter.")
                    elif guess in sentence:
                        print(f"Good guess! The letter '{guess}' is in the sentence.")

                        for i, char in enumerate(sentence):
                            if char == guess:
                                revealed_sentence[i] = guess
                    else:
                        print(f"Wrong guess! The letter '{guess}' is not in the sentence.")
                        hangman_progress += "HANGMAN"[len(hangman_progress)]

                    guessed_letters.add(guess)

                    if "_" not in revealed_sentence:
                        print("Congratulations! You've guessed the sentence:")
                        print(revealed_sentence)
                        return


                print("You've been hanged! The word 'HANGMAN' is complete.")
                print("The correct sentence was:", sentence)


    def print_sentence_hangman(self, sentence):
        words = sentence.split()
        result = []

        for word in words:
            if len(word) > 1:
                first_letter = word[0]
                last_letter = word[-1]
                revealed_word = [
                    char if char == first_letter or char == last_letter else '_'
                    for char in word
                ]
            else:

                revealed_word = [word]
            result.extend(revealed_word + [' '])

        if result[-1] == ' ':
            result.pop()

        return result




