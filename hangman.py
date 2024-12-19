import random
from words import word_list


def get_word(): # Selects a random word from word_list.
    word = random.choice(word_list)
    return word.upper() 


def play(word):
    word_completion = "_" * len(word) # If the word has 4 letters, it prints 4 underscores: ____
    guessed = False # User did not guess yet.
    guessed_letters = [] # The letters that user guess
    guessed_words = [] # Contains the guessed words
    tries = 6 # Total tries that user has
    print("Let's play Hangman!")
    print(display_hangman(tries)) # Displays the head, body, arms, legs.
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): # Checks if guess is a single alphabet letter.
            if guess in guessed_letters: # Checks if the letter was already guessed.
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess) 
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess] # Finds the positions of the guessed letter in the word.
                for index in indices:
                    word_as_list[index] = guess # Replace underscores with correctly guessed letter.
                word_completion = "".join(word_as_list)
                if "_" not in word_completion: # no underscore means the word is guessed.
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): # Checks if the guess is the correct length.
            if guess in guessed_words: 
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess) # add guessed word to list
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word() # Random word pulled from list of words.
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y": #upper function makes letters into uppercase
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()