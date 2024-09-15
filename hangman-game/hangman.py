# package to generate random words
from random_word import RandomWords

# importing hangman ascii art 
from hangman_visual import lives_visual_dict

# Function to get a random word
def get_word():
    r = RandomWords()
    random_word = r.get_random_word()

    return random_word

# Function to get a validated user input
def user_input(): 
    while True:
        user_letter = input("Guess a letter: ").upper()

        if not(user_letter.isalpha()):
            print("Please enter a letter!!")
            continue
        elif len(user_letter) > 1:
            print("Only one letter please!!")
            continue
        else:
            break
    
    return user_letter

# Function to display the current state of the word
def display_word(word, correct_letters): 
    display = ''

    for letter in word:
        if letter in correct_letters:
            display += letter
        else:
            display += '_ '

    return display

# Main function to run the hangman game
def hangman():

    random_word = get_word().upper()

    correct_letters = []  # List to store correctly guessed letters
    letters_used = [] # List to store all guessed letters
    correct_word = '' # String to store the current state of the word
    attempts = 7 # Number of attempts allowed

    print(f"Welcome to the hangman game\nThe word is {len(random_word)} letters long\nYou have 7 tries\nGet going!!!")

    while attempts > 0:

        print(f"Attempts left: {attempts}")

        guessed_letter = user_input().upper()

        if guessed_letter in letters_used:
            print("You've already used this letter")
            attempts -= 1

        elif guessed_letter not in random_word:
            print("Incorrect letter")
            letters_used.append(guessed_letter)
            attempts -= 1

        elif guessed_letter in random_word:
            correct_letters.append(guessed_letter)
            letters_used.append(guessed_letter)
        
        correct_word = display_word(random_word, correct_letters)

        print(correct_word)

        print(lives_visual_dict[attempts])

        if correct_word == random_word:
            break
    
    # Final message based on the game outcome
    if attempts == 0: 
        print("\nSorry you're dead!!")
        print(f"The word was {random_word}")
    else:
        print("\nCongrats!! You guessed the correct letters")

# Entry point of the script
if __name__ == '__main__':
    hangman()