import random


Max_value = 100
Min_value = 1


# function generates number between minimum and maximum value.
def generate_number(min: int, max: int):
    return random.randint(min, max)


# function asks input from user and checks if its higher, lower or equal to the generated number.
def guess_number(number: int, max: int, min: int):
    while True:
        guess = input("Guess a number between 1 and 100 or press 0 to exit: ")
        try:
            guess = int(guess)
            if guess <= max and guess >= min:
                if (guess < number + 5 and guess > number - 5) and guess != number:
                    print("You're close!\n")
                elif guess < number:
                    print("Too low.\n")
                elif guess > number:
                    print("Too high.\n")
                elif guess == number:
                    print("Congrats you guessed right!\n")
                    break
            # if the user types the number 0 it will give the user the option to generate a new number or quit.
            elif guess == 0:
                return False
            else:
                print("Number is out of bounds.")
        except ValueError:
            print("Please input an integer.")


# function that allows user to choose to replay the game or not.
def replay():
    while True:
        retry = input("Play again? (Y/N) ".lower())
        if retry == "y":
            return True
        if retry == "n":
            return False
        else:
            print("Invalid input.")
            continue


# main game loop
def game_loop():
    while True:
        guess_number(generate_number(Min_value, Max_value), Max_value, Min_value)
        if replay() == False:
            break
    print("Thanks for playing!\n")


game_loop()
