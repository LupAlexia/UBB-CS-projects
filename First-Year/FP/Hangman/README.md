# Hangman – Python Project

A classic **Hangman** word-guessing game implemented in Python using object-oriented design. Developed as part of the **First-Year Fundamental Programming** module at UBB.

---

## 🎯 Game Description

- A secret word is randomly selected from a predefined list.
- The player guesses **one letter at a time**.
- Correct guesses reveal letters in the word.
- Incorrect guesses build a “hangman” displayed step-by-step (or count of mistakes).
- The player loses after a maximum number of wrong guesses (e.g., 6).
- The player wins by guessing all letters correctly before reaching the limit.

---

## Game Commands & Flow
- Guess a letter when prompted
- The game responds with the updated word status
- Faults increase with each incorrect guess. You lose after too many faults.
- When all letters are guessed, you win and the game ends.

---

## Features
- OOP design: clear separation of Game logic and UI
- Word list loaded from words.txt
- Input validation: handles non-alphabet input, repeat guesses
- Handles uppercase/lowercase equivalently
