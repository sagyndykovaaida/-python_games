import random

# List of words to choose from
words = ['apple', 'banana', 'cherry', 'orange', 'pear']

# Choose a random word from the list
word = random.choice(words)

# Create a list to store the letters guessed by the user
guesses = []

# Set the number of chances for the user to guess the word
chances = 6

# Loop until the user guesses the word or runs out of chances
while chances > 0:
    # Display the word with dashes for unguessed letters
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "-"
    print(display)
    
    # Prompt the user to guess a letter
    guess = input("Guess a letter: ")
    
    # Check if the letter has already been guessed
    if guess in guesses:
        print("You already guessed that letter.")
    else:
        guesses.append(guess)
        
        # Check if the letter is in the word
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            chances -= 1
            
    # Check if the user has guessed the word
    if set(word) == set(guesses):
        print("Congratulations, you guessed the word!")
        break
    
# If the user runs out of chances, display the correct word
if chances == 0:
    print("Sorry, you ran out of chances. The word was", word)