import random
word_list = ["mango", "elephant", "batman", "rose", "mercury"]

hints = [
    "A fruit",
    "An animal",
    "A superhero",
    "A flower",
    "A planet"
]

print("\U0001F3AE Welcome to Hangman game!") # 🎮
print("Guess the word one letter at a time.")
print("You have 6 wrong guesses.")

play_again = "yes"

while play_again == "yes":

    word_index = random.randint(0, len(word_list) - 1)
    secret_word = word_list[word_index]
    hint = hints[word_index]

    hidden_word = ["_"] * len(secret_word)
    guessed_letters = []
    wrong_guesses = 0

    print("\n\U0001F4A1 Hint:", hint)


    while wrong_guesses < 6 and "_" in hidden_word:

        print("\nWord:", " ".join(hidden_word))
        print("Wrong guesses:", wrong_guesses, "/ 6")
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        if len(guess)!= 1:
            print("Enter only 1 letter!")
            continue
        if not guess.isalpha():
            print("Only letters allowed!")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess! \U00002705") 
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    hidden_word[i] = guess
        else:
            print("Wrong guess! \U0000274C") 
            wrong_guesses += 1

    
    if "_" not in hidden_word:
        print("\n\U0001F389 You won!") 
        print("The word was:", secret_word)
    else:
        print("\n\U0001F480 Game over!") 
        print("The word was:", secret_word)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

print("\nThanks for playing! \U0001F44B") 
