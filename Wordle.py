import random
import turtle
class Wordle:

    def __init__(self):
        self.words = self.load_words()
        self.target = ""

    def load_words(self):
        """Description: The function opens a text file and loads the words into a list while ensuring all words are the same length and contains no bad characters or numbers. Takes a filename string with .txt extention as a parameter and returns 'word_list' at the end."""
        file = open("words.txt", "r")

        #### Initializing variables, lists, etc...
        word_length = 0
        first_line = True  # Used for the if statement in the for loop.
        word_list = []  # Returning list
        modified_line = ""  # Meant for modifying the each line (to remove blanc spaces, new line characters, etc)

        #### Takes each line (in this case the word) from the text file and runs through a series of checks (if else statements).
        for line in file:

            # Checks the length of the first line's word which will be stored to a variable 'word_length' to compare for the remaining words in the text file.
            if first_line == True:
                modified_line = line.strip()  # Removes all whitespaces, new line characters.
                word_length = len(modified_line)  # Set's the word length restriction for the rest of the words.
                first_line = False  # Ensure this if statement is never run again

            # Runs, if not first line of the txt file:
            else:
                # Check: Current word matches the first word's word_length
                if len(line.strip()) != word_length:
                    return False

                # Otherwise strip all whitepsaces and save it to modified_line.
                else:
                    modified_line = line.strip()

            #### Check each letter of the word for bad characters (includes anything that is not a alphabet)
            for character in line.strip():

                # Ord range 65-91 is equivalent from A to Z. If a letter not in this range it must be a bad character or a number.
                if ord(character.upper()) not in range(65, 91):
                    return False

            word_list.append(modified_line)  # Add word to the word_list.

        #### Check if the list was empty which means txt file was empty too
        if len(word_list) == 0:
            return False

        file.close()

        return word_list

    def choose_word(self,wordlist):
        """Description: Chooses a random index from the list that is returned from the load_words function or return false if the list was empty. Takes in 'word_list' as a parameter and returns either False or an integer value."""

        #### If list is empty
        if not wordlist:
            return False

        #### Randomly generates a index value from 0 to list's length minus 1
        else:
            return wordlist[random.randint(0, len(wordlist) - 1)]

    def score_guess(self, guess, target, words):
        # String will be concatenated with symbols below
        color_list = []

        #### Evaluates each letter in guess
        for letter in range(len(guess)):
            # If letter is matching the target letter at the same index
            if guess[letter].lower() == target[letter].lower():
                color_list.append("green")
            
            # If letter is matching the target letter at a different index
            elif guess[letter].lower() in target:
                color_list.append("yellow")
            
            # Otherwise the letter doesn't exist in target
            else:
                color_list.append("grey")
        
        return color_list

    def draw_grid(self,attempt, result_list=[], guess_list=[]):
        if attempt == 1:
            x = -170
            y = 200
            for row in range(5):
                for col in range(5):
                    t.penup()
                    t.goto(x,y)
                    t.pendown()
                    t.forward(50)
                    t.right(90)
                    t.forward(50)
                    t.right(90)
                    t.forward(50)
                    t.right(90)
                    t.forward(50)
                    t.right(90)
                    t.penup()
                    x+=70
                x = -170
                y -= 70
        
        else:
            x = -170
            y = 200
            for row in range(5):
                for col in range(5):
                    if row+1 < attempt:
                        t.penup()
                        t.goto(x,y)
                        t.pendown()
                        t.fillcolor(result_list[row][col])
                        t.begin_fill()
                        t.forward(25)
                        t.penup()
                        t.right(90)
                        t.forward(40)
                        t.left(90)
                        t.pendown()
                        t.write(f"{guess_list[row][col]}", align="center", font=("Arial", 30, "bold"))
                        t.penup()
                        t.left(90)
                        t.forward(40)
                        t.right(90)
                        t.pendown()
                        t.forward(25)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.end_fill()
                        t.penup()
                        x+=70
                    else:
                        t.penup()
                        t.goto(x,y)
                        t.pendown()
                        t.forward(50)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.forward(50)
                        t.right(90)
                        t.penup()
                        x+=70
                x = -170
                y -= 70
        screen.update()

    def write_wordle(self, attempt):
        t.goto(0,280)
        t.write("Wordle", align="center", font=("Arial", 50, "bold"))

        if attempt != 1:
            t.pencolor("white")
            t.goto(0,260)
            t.pendown()
            t.fillcolor("white")
            t.begin_fill()
            t.forward(70)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(140)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(70)
            t.end_fill()
            t.penup()
            t.pencolor("black")

        t.goto(0,260)
        t.pendown()
        t.write(f"Attempt {attempt} of 5", align="center", font=("Arial", "20"))


# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
WINDOW_TITLE = "Wordle Game"

# Set up the screen object
turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)

# Turn off screen updates for faster drawing
screen.tracer(0)

# Create the turtle object
t = turtle.Turtle()
t.pensize(3)
t.hideturtle()
turtle.Screen().bgcolor("white")
t.speed(0)
t.penup()



### GAME STARTS
running = True
while running:
    t.pencolor('black')
    user = Wordle()
    won = False
    attempt = 1
    target = user.choose_word(user.load_words())
    result_list = []
    guess_list = []
    print(target)
    while attempt <= 5:
        if attempt != 1:
            user.write_wordle(attempt)
            user.draw_grid(attempt, result_list, guess_list)
            screen.update()
        else:
            user.write_wordle(attempt)
            user.draw_grid(attempt)
            screen.update()
        if attempt != 1 and guess.upper() == target.upper():
            won = True
            break
        guess = str(screen.textinput(f"ATTEMPT {attempt}", "Guess a valid 5 letter word: "))
        while len(guess) != 5 or not guess.isalpha() or guess not in user.words:
            t.pencolor("red")
            if len(guess) != 5:
                t.goto(0,220)
                t.write(f"'{guess}' is not a 5 letter word", align="center", font=("Arial", "15"))
                screen.update()

            elif guess.isalpha():
                t.goto(0,220)
                t.write(f"'{guess}' is not a word", align="center", font=("Arial", "15"))
                screen.update()

            elif guess.lower() not in user.words:
                t.goto(0,220)
                t.write(f"'{guess}' is not in word list", align="center", font=("Arial", "15"))
                screen.update()

            guess = screen.textinput(f"ATTEMPT {attempt}", "Guess a valid 5 letter word: ")
            t.pencolor("white")
            t.goto(0,210)
            t.pendown()
            t.fillcolor("white")
            t.begin_fill()
            t.forward(90)
            t.left(90)
            t.forward(40)
            t.left(90)
            t.forward(180)
            t.left(90)
            t.forward(40)
            t.left(90)
            t.forward(90)
            t.end_fill()
            t.penup()
            screen.update()
        t.pencolor("black")
        guess_list.append(list(guess.upper()))
        result_list.append(user.score_guess(guess,target,user.words))
        attempt += 1

    if won:
        t.goto(0,-200)
        t.pendown()
        t.pencolor(0.5, 1, 0.5)
        t.write(f"Congratulations!", align="center", font=("Arial", 30, "bold"))
        t.penup()
        t.goto(0,-250)
        t.pendown()
        t.pencolor("black")
        t.write("You guess the correct word,", align="center", font=("Arial", 20, "bold"))
        t.penup()
        t.goto(0,-295)
        t.pendown()
        t.pencolor("blue")
        t.write(f"'{target.upper()}'", align="center", font=("Arial", 40, "bold"))
        t.penup()
        t.goto(0,-320)
        t.pendown()
        t.pencolor("black")
        t.write(f"In {attempt-1} attempts!", align="center", font=("Arial", 15, "bold"))

    else:
        user.draw_grid(attempt, result_list, guess_list)
        t.goto(0,-200)
        t.pendown()
        t.pencolor(0.5, 1, 0.5)
        t.write(f"Oh no!", align="center", font=("Arial", 30, "bold"))
        t.penup()
        t.goto(0,-250)
        t.pendown()
        t.pencolor("black")
        t.write("You failed to guess,", align="center", font=("Arial", 20, "bold"))
        t.penup()
        t.goto(0,-295)
        t.pendown()
        t.pencolor("blue")
        t.write(f"'{target.upper()}'", align="center", font=("Arial", 40, "bold"))
        t.penup()
        t.goto(0,-320)
        t.pendown()
        t.pencolor("black")
        t.write(f"GAME OVER!", align="center", font=("Arial", 15, "bold"))
        t.penup()

    choice = str(screen.textinput(f"Another Game?", "Would you like to play another game [Y/N]? "))
    if choice.upper() != "Y":
        running = False
        screen.clear()
        screen.update()
        
    screen.clear()
    screen.update()


# Make a clean exit
screen.exitonclick()
turtle.done()