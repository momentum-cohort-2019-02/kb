from random import randint

MAX_NUM = 1000


def respond_to_guess(actual, guess):
    if guess < actual:
        print("Too low!")
    elif guess > actual:
        print("Too high!")
    else:
        print("You got it right!")


def get_guess():
    while True:
        user_input = input("Make a guess between 1 and 100: ")
        if user_input.isnumeric():
            guess = int(user_input)
            if 1 <= guess <= MAX_NUM:
                return guess
        print("That was not a valid guess.")


def run_game():
    """Run the main game loop."""

    number_to_guess = randint(1, MAX_NUM)
    print(f"""
    I have chosen a random number between 1 and {MAX_NUM}.
    You need to guess this number.
    I will let you know if your guess is too high or too
    low and tell you how many guesses you've used.
    """)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = get_guess()
        respond_to_guess(number_to_guess, guess)
        attempts += 1

    print(f"That took you {attempts} attempts.")


if __name__ == "__main__":
    run_game()
