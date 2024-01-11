lives = 3
word = list("Apple".lower())
correctguesses = []
alreadyguessed = []

def printguess():
    for i in range(len(correctguesses)):
        print(correctguesses[i], end=" ")
    print("")

def checkguess(guess):
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                correctguesses[i] = guess
        print("Correct!")
    else:
        print("Wrong!")
        global lives
        lives = lives - 1
        print("Incorrect guessed letters: "+str(alreadyguessed[-1]))
        print("You have "+str(lives)+" lives left")
        if lives == 0:
            print("You lose!")
            exit()
def checkwin():
    for i in range(len(word)):
        if word[i] != correctguesses[i]:
            return False
    return True

try:
    lives = int(input("How many lives do you want? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

word = input("Please enter a word: ").lower()

# clear the screen
print("\n"*100)

# initialize the correctguesses list with the same length as the word and fill it with underscores
for i in range(len(word)):
    correctguesses.append("_")

while lives > 0:
    guess = input("Please enter a letter: ").lower()
    if (len(guess) != 1):
        print("Please enter a single letter")
        continue
    elif (guess in alreadyguessed):
        print("You already guessed this letter")
        continue
    else:
        alreadyguessed.append(guess)

    checkguess(guess)
    printguess()

    if checkwin():
        print("You win! ❤️")
        exit()
