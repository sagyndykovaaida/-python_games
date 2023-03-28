import random

words = ['apple', 'banana', 'cherry', 'orange', 'pear']

word = random.choice(words)

guesses = []

chances = 6

while chances > 0:
    display = ""
    for letter in word:
        if letter in guesses:
            display += letter
        else:
            display += "-"
    print(display)
    
    guess = input("Guess a letter: ")
    
    if guess in guesses:
        print("You already guessed that letter.")
    else:
        guesses.append(guess)
        
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            chances -= 1
            
    if set(word) == set(guesses):
        print("Congratulations, you guessed the word!")
        break
    
if chances == 0:
    print("Sorry, you ran out of chances. The word was", word)