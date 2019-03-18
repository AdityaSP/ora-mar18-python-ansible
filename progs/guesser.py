import random
r = random.randint(0,100)
print("I have a number. Its your turn to guess now!")
guesses=[]

while True:
    ui = int(input("Enter your guess(0,100): "))
    guesses.append(ui)    
    if ui < r:
        print("Low")
    elif ui > r:
        print("High")
    else:
        print("Bingo! You guessed it right!")
        print("You took ", len(guesses), "guesses.")
        print("These were your gueses", guesses)
        break

# 1. print the number of guesses taken
# 2. print all the tries.        