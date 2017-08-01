def guessingGame():
    import random
    myNum = random.randint(1, 10)
    print("Guess number between 1-10.")
    max_guesses = 3
    guessesLeft = max_guesses

    while guessesLeft:
        guess = int(input("Guess a number: "))
        guessesLeft -= 1
        if guess == myNum:
            print("You Got It!")
            break
        elif (guess == myNum - 1) or (guess == myNum + 1):
            print("It's Hot")
        elif (guess == myNum - 2) or (guess == myNum + 2):
            print("It's Warm")
        elif guess != myNum:
            print("It's Cold")
        if guessesLeft == 0:
            print("The guess number was", myNum)
guessingGame()

end = input("Want to try agian? ")
while end == 'yes' or end == 'yea' or end == 'y':
    guessingGame()
print("Bye Bye!")