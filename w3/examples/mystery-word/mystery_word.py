word_to_guess = "racecar"
letters_guessed = []


def word_guessed(word_to_guess, letters_guessed):
    """
    Given a word to guess and a list of the letters currently guessed,
    return True if all the letters in the word have been guessed already.
    """
    for letter in word_to_guess:
        if letter not in letters_guessed:
            return False
    return True


def is_letter_input(user_input):
    return len(user_input) == 1 and user_input.isalpha()


def get_letter_input():
    user_input = input("Type a letter to guess: ").casefold()
    while not is_letter_input(user_input):
        print("That was not a letter.")
        user_input = input("Type a letter to guess: ").casefold()

    return user_input


if __name__ == "__main__":
    while not word_guessed(word_to_guess, letters_guessed):
        letter_guessed = get_letter_input()
        letters_guessed.append(letter_guessed)
