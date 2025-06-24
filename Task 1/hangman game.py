import random

# Predefined list of words
word_list = ["apple", "grape", "mango", "peach", "lemon"]

# Randomly choose a word
word_to_guess = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display hidden word with underscores
display_word = ["_"] * len(word_to_guess)

print("Welcome to Hangman!")

while incorrect_guesses < max_guesses and "_" in display_word:
    print("\nWord: ", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print(f"Wrong! You have {max_guesses - incorrect_guesses} guesses left.")

# End of game messages
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word_to_guess)
else:
    print("\nGame Over! The word was:", word_to_guess)
