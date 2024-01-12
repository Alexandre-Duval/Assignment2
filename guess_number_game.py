import random


Max_value = 100
Min_value = 1


# function generates number between minimum and maximum value.
def generate_number(min: int, max: int) -> int:
    return random.randint(min, max)


# function asks input from user and checks if its higher, lower or equal to the generated number.
def guess_number(generate_number: int, max: int, min: int) -> int:
    while True:
        guess = input("Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
            if guess <= max and guess >= min:
                if guess < generate_number + 5 and guess > generate_number - 5:
                    print("You're close!")
                elif guess < generate_number:
                    print("Too low.")
                elif guess > generate_number:
                    print("Too high.")
                elif guess == generate_number:
                    print("Congrats you guessed right!")
                    return False
            # if the user types the number 0 it will allow them quit the game.
            elif guess == 0:
                return False
            else:
                print("Number is out of bounds.")
        except ValueError:
            print("Please input an integer.")


# function that allows user to choose to replay the game or not.
def replay() -> bool:
    while True:
        retry = input("Would you like to play again? (Y/N) ")
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
    print("\nThanks for playing!\n")


game_loop()
