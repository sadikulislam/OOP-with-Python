import random

low = 1
high = 100
max_attempts = 10

secret_number = random.randint(low, high)


def guess_number():
    while True:
        try:
            guess = int(input(f"==> Guess a number between {low} and {high}: "))
            if low <= guess <= high:
                return guess
            else:
                print("Invalid input. Please enter a number within the specified range.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"


def play_game():
    attempts = 0
    won = False

    while attempts < max_attempts:
        attempts += 1
        guess = guess_number()
        result = check_guess(guess, secret_number)

        if result == "Correct":
            print(f"Congratulations! You guessed the number {secret_number}.")
            won = True
            break
        else:
            print(f"{result}. Try again!")

    if not won:
        print(f"Sorry, you ran out of attempts! The secret number is {secret_number}.")


print("<==============> Welcome to the Number Guessing Game! <=================>")
play_game()
