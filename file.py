import random
print("Number Guessing Game")
number= random.randint(1,9)
print("Guess A Number Between 1 and 9")
chances=0
while chances<5:
    guess=int(input("Enter your Guess "))
    if guess==number:
        print("Congratulations You won")
        break
    elif guess<number:
        print("Your Guess Was Too Low. Guess A number Higher Than ", guess)
    else:
        print("Your Guess Was Too High. Guess A number Lower Than ", guess)
    chances=chances+1

if not chances<=5:
    print("You Lost The Number is ", number)