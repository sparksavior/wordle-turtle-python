
# Wordle Game

A Python implementation of the popular word game Wordle, featuring a graphical interface using the `turtle` module. The game reads words from a text file and provides a grid-based interface for guessing.

---

## Features

- A grid-based Wordle game built using `turtle` graphics.
- Customizable word list loaded from a text file (`words.txt`).
- Feedback on each guess:
  - **Green:** Correct letter in the correct position.
  - **Yellow:** Correct letter in the wrong position.
  - **Gray:** Letter not in the word.

---

## Requirements

- Python 3.x  
- `turtle` module (comes pre-installed with Python)  
- A text file named `words.txt` containing the word list.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <REPO_URL>
   cd <REPO_DIRECTORY>
   ```

2. Ensure `Wordle.py` and `words.txt` are in the same folder.  
3. Run the game:
   ```bash
   python Wordle.py
   ```
4. Enter your guesses directly in the pop-up input box.  
5. Follow the on-screen instructions to complete the game.

---

## Example Gameplay

1. **Grid Setup:**  
   The game sets up a 5x5 grid and prompts you to guess a word.

2. **Enter Your Guess:**  
   Input a valid 5-letter word. Feedback will be displayed based on your guess:
   - **Green:** Correct letter and position.
   - **Yellow:** Correct letter but wrong position.
   - **Gray:** Letter not in the word.

3. **Win or Lose:**  
   - If you guess the word in 5 attempts or fewer, you win!
   - Otherwise, the game ends with the correct word revealed.

---

## Customizing the Word List

You can modify the `words.txt` file to include your own list of 5-letter words. Ensure:
- All words have exactly 5 letters.  
- The file does not contain any special characters, numbers, or blank lines.

---

## Running Tests

To test the game:

1. Add a valid word list to `words.txt`.  
2. Run the script:
   ```bash
   python Wordle.py
   ```
3. Verify the gameplay functionality, including grid drawing and feedback.

---

## Additional Git Commands

1. Initialize the repository:
   ```bash
   git init
   ```

2. Add files to the repository:
   ```bash
   git add Wordle.py words.txt README.md .gitignore LICENSE
   ```

3. Commit changes:
   ```bash
   git commit -m "Initial commit: Wordle game implementation"
   ```

4. Create a remote repository on GitHub and push:
   ```bash
   git remote add origin <REPO_URL>
   git branch -M main
   git push -u origin main
   ```

---

## Notes

- The game automatically validates guesses for correct length and word validity.  
- `words.txt` must contain at least one valid 5-letter word, or the game will not start.

---

## License

This project is open-source and available under the MIT License.

---

## Happy Wordling! 🎮
