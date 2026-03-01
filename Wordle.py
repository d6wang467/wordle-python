import random  #randomly select a word and reward/punishment

#read words from a text file and returns as a list
def load_dictionary(file_path):
    with open(file_path) as f:  #open the file
        words = [line.strip().lower() for line in f]  #remove newline + lowercase
    return words  # return list of words

#checks whether a guess is valid
def is_valid_guess(guess, guesses):
    #must be 5 letters, alphabetic, and exist in the guess list
    return len(guess) == 5 and guess.isalpha() and guess in guesses

#compares the guess to the secret word and returns the colors
def evaluate_guess(guess, word):
    result = ""  #string that will store colored letters

    #loop through each of the 5 positions
    for i in range(5):

        #if letter matches exactly (correct letter + position)
        if guess[i] == word[i]:
            result += "\033[32m" + guess[i]   # green

        #if letter exists somewhere else 
        elif guess[i] in word:
            result += "\033[33m" + guess[i]   # yellow

        #if letter is not in the word at all
        else:
            result += "\033[0m" + guess[i]    # normal color
    
    #reset terminal color at the end
    return result + "\033[0m"

#main game function
def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")

    #randomly choose a secret word from the answer list
    secret_word = random.choice(answers)

    #reward messages if user wins
    treats = [
        "🍪 Eat your favorite snack!",
        "📺 Binge watch for 2 hours!",
        "🥂 Go out tonight!",
        "😴 Take a nap!"
    ]

    #challenge messages if user loses
    challenges = [
        "💪 Do 5 pushups.",
        "🦵 Do 20 jumping jacks.",
        "🧘 Hold a 20-second plank.",
        "🧱 2 minute wall sit."
    ]

    attempts = 1  #start attempt counter
    max_attempts = 6  #maximum allowed guesses

    #game loop (runs until the 6th attempt)
    while attempts <= max_attempts:

        #get user input,remove spaces,convert to lowercase
        guess = input("Enter Guess #" + str(attempts) + ": ").lower().strip()
        
        #validate guess
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter a 5-letter English word.")
            continue  # do not count invalid guesses

        #print the feedback with colors 
        print(evaluate_guess(guess, secret_word))

        #check if user guessed correctly
        if guess == secret_word:
            print("🎉 Congratulations! You guessed the word:", secret_word)
            print(random.choice(treats))  # randomly select a reward
            return  #end the game early if correct

        attempts += 1  #increment attempt counter

    #if loop ends without a correct guess
    print("Game over. The secret word was:", secret_word)
    print(random.choice(challenges))  #randomly select a challenge

#word list for appropriate guesses and answers 
guesses = load_dictionary("wordle_possibles.txt")
answers = load_dictionary("wordle-answers-alphabetical.txt")

#calling the game to start 
wordle(guesses, answers) 