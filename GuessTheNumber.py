#Guess the Numer Game

#imports
import random
import time


#game variables
player_guesses = 1
comp_guesses = 1
player_score = 0
computer_score = 0
rounds = 0
p = 0
num = random.randint(1, 10)
c = random.randint(1, 10)

#def for start of game to be called at the end of each game
def game_start():
    #global variable so it can be altered outside the defined variable.
    global rounds
    time.sleep(1.4)
    start = input("Would you like to play?(Y/N) ").lower()
    # Possible answers
    if start == 'y':
        rounds +=1
        print("let's Play")
        time.sleep(.5)
        print(f"(Round{rounds})")
    elif start == 'n':
        if rounds == 0:
            print('Okay, bye')
        elif rounds != 0:
            print(f"You played {rounds} rounds, and beat Cybernet {player_score} times")
            quit()
    else:
        print("Please say (Y/N)")
        print()
        game_start()


#start of game
print("This is a guessing game, You will compete against a computer to see who can guess the number the fastest!")
game_start()
while True:
    time.sleep(.2)
    print("Guess a number between 1-10: ")
    p = (int(input("")))
    if p < num:
        player_guesses += 1
        print("You guessed to low, guess again: ")
    elif p > num:
        player_guesses += 1
        print("You guessed to high, guess again: ")
    else:
        print("Well done you guessed it!")
        print("You guessed it in", player_guesses, "attempts!")

        #computers turn to guess
        print()
        print("The computer is guessing against you.......")
        time.sleep(2)
        y = num
        z = c
        if c < num:
            comp_guesses += 1
            z = z + 1
            c = random.randint(z, y)
            if c < num:
                comp_guesses += 1
                z = z + 1
                c = random.randint(z, y)
                if c < num:
                    comp_guesses += 1
                    z = z + 1
                    c = random.randint(z, y)
                    if c < num:
                        comp_guesses += 1
                        z = z + 1
                        c = random.randint(z, y)
                        if c < num:
                            comp_guesses += 1
                            z = z + 1
                            c = random.randint(z, y)
                            if c < num:
                                comp_guesses += 1
                                z = z + 1
                                c = random.randint(z, y)

        elif c > num:
            comp_guesses += 1
            z = z - 1
            c = random.randint(y, z)
            if c > num:
                comp_guesses += 1
                z = z - 1
                c = random.randint(y, z)
                if c > num:
                    comp_guesses += 1
                    z = z - 1
                    c = random.randint(y, z)
                    if c > num:
                        comp_guesses += 1
                        z = z - 1
                        c = random.randint(y, z)
                        if c > num:
                            comp_guesses += 1
                            z = z - 1
                            c = random.randint(y, z)
                            if c > num:
                                comp_guesses += 1
                                z = z - 1
                                c = random.randint(y, z)

        if c == num:
            print("The computer guessed it in", comp_guesses, "attempts")
            if comp_guesses > player_guesses:
                print("You beat cybernet, great job John connor!")
                player_score += 1
                print()
                game_start()
            elif comp_guesses < player_guesses:
                print("You lost, cybernet is victorious.")
                computer_score += 1
                print()
                game_start()
            else:
                print("its a tie, you must go again.")
                print()
                game_start()