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
    """
    Check to see if the input is one character long and is a letter.
    """
    return len(user_input) == 1 and user_input.isalpha()


def get_letter_input():
    user_input = input("Type a letter to guess: ").casefold()
    while not is_letter_input(user_input):
        print("That was not a letter.")
        user_input = input("Type a letter to guess: ").casefold()

    return user_input


def get_display_word(word, letters_to_show):
    """Given a word being guessed and the letters currently guessed,
    display that word as a series of space-separated underscores (if the
    current letter has not been guessed) or the current letter, uppercased.
    """
    output_chars = []
    for letter in word:
        if letter in letters_to_show:
            output_chars.append(letter.upper())
        else:
            output_chars.append("_")
    return " ".join(output_chars)


if __name__ == "__main__":
    word_to_guess = "racecar"
    letters_guessed = []

    while not word_guessed(word_to_guess, letters_guessed):
        print(get_display_word(word_to_guess, letters_guessed))
        letter_guessed = get_letter_input()
        letters_guessed.append(letter_guessed)

    print(get_display_word(word_to_guess, letters_guessed))
    print("You won!")
