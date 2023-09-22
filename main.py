import random

LEXICON_FILE = 'Lexicon.txt'
INITIAL_GUESSES = 8

def get_word():
    with open(LEXICON_FILE, 'r') as file:
        word_list = file.read().splitlines()
    
    return random.choice(word_list)

# Rest of the code remains the same as before
def play_game(secret_word):
    # Initialize game variables
    #guessed_letters = []
    incorrect_guesses = 0
    dashes = ['-'] * len(secret_word)
    
    # Print game instructions
    print_instructions(INITIAL_GUESSES)
    
    # Game loop
    while incorrect_guesses < INITIAL_GUESSES:
        display_game_state(dashes, incorrect_guesses, INITIAL_GUESSES)
        guess = get_user_guess()
        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Guess should only be a single letter. Try again!")
            print()
            continue
        
        if guess in secret_word:
            update_dashes(guess, secret_word, dashes)
            print("That guess is correct.")
            if '-' not in dashes:
                # All letters have been guessed correctly
                print("\033[92mCongratulations!\033[0m You guessed the word correctly. The secret word is: \033[92m", secret_word,"\033[0m")
                break
        else:
            # Incorrect guess
            incorrect_guesses += 1
            print("\033[92mThere is\033[0m \033[38;5;196mno \033[92m",guess,"'s in the word\033[0m")
            print()
    
    if '-' in dashes:
        # Player has run out of guesses
        print("\033[92mSorry\033[0m, you lost. The secret word was: \033[92m",secret_word,"\033[0m")

# Main function

def print_instructions(INITIAL_GUESSES):
    print("Welcome to WordGuess!")
    print("Guess the letters to uncover the secret word.")
    print("\033[92mYou have \033[38;5;208m",INITIAL_GUESSES,"\033[0m \033[92mchances to guess the word.\033[0m")
    print("Let's begin!")
    print()
    
def display_game_state(dashes, incorrect_guesses, INITIAL_GUESSES):
    print("\033[0mThe word now looks like this:", ' '.join(dashes))
    print("\033[92mYou have \033[38;5;208m", INITIAL_GUESSES - incorrect_guesses, "\033[0m \033[92mguesses left")

    
def get_user_guess():
    return input("\033[92mType a single letter here\033[0m, then press enter: \033[92m").upper()

def update_dashes(guess, secret_word, dashes):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            dashes[i] = guess
 
    
def main():
    secret_word = get_word()
    play_game(secret_word)

if __name__ == '__main__':
    main()
