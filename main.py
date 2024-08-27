    '''
This is a very Simple Micro Project(The Perfect Guess) which generates a random number and asks the user to guess it.
If the player's guess is higher than the actual number, program displays: "Lower Number Please".
Similarly, if the player's guess is low, the program displays: "Higher Number Please".
When the player guesses the correct number, the program displays the number of guesses used to arrive at the number.
(Note: Random Module is used in this Program)
    '''


import random    # -->    Importing Random Module

n = random.randint(1, 100) 
a = -1
guesses = 1

while(a != n):
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")



# Game Over
