import random


def word_guessed(word_to_guess, letters_guessed):
    """
    Given a word to guess and a list of the letters currently guessed,
    return True if all the letters in the word have been guessed already.
    """
    for letter in word_to_guess.lower():
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
    for letter in word.lower():
        if letter in letters_to_show:
            output_chars.append(letter.upper())
        else:
            output_chars.append("_")
    return " ".join(output_chars)


def get_word_list(filename):
    """
    Given a file with words on each line, get a list of those words.
    """
    with open(filename) as file:
        word_list = [line.strip().lower() for line in file]

    return word_list


def filter_word_list_by_difficulty(word_list, difficulty):
    """
    Given a list of words and a difficulty level, filter
    that list.
    easy -> length 4-6
    medium -> length 6-8
    hard -> length 8+
    """
    filtered_word_list = []
    for word in word_list:
        if difficulty == 'easy' and 4 <= len(word) <= 6:
            filtered_word_list.append(word)
        if difficulty == 'medium' and 6 <= len(word) <= 8:
            filtered_word_list.append(word)
        if difficulty == 'hard' and len(word) >= 8:
            filtered_word_list.append(word)

    return filtered_word_list


def game_over(word_to_guess, letters_guessed, guesses_left):
    return word_guessed(word_to_guess, letters_guessed) or guesses_left == 0


if __name__ == "__main__":
    difficulty = None
    while difficulty not in ['easy', 'medium', 'hard']:
        difficulty = input(
            "What difficulty would you like? (easy, medium, or hard) ")
    print(f"You chose {difficulty}.")

    word_list = get_word_list('words.txt')
    word_list = filter_word_list_by_difficulty(word_list, difficulty)
    word_to_guess = random.choice(word_list)
    letters_guessed = []
    guesses_left = 8

    while not game_over(word_to_guess, letters_guessed, guesses_left):
        print(get_display_word(word_to_guess, letters_guessed))
        letter_guessed = get_letter_input()
        if letter_guessed in letters_guessed:
            print("You have already guessed that letter.")
        elif letter_guessed in word_to_guess:
            print("You guessed a correct letter.")
            letters_guessed.append(letter_guessed)
        else:
            letters_guessed.append(letter_guessed)
            guesses_left -= 1
            print(f"Bad choices. {guesses_left} guesses left.")

    if word_guessed(word_to_guess, letters_guessed):
        print(get_display_word(word_to_guess, letters_guessed))
        print("You won!")
    else:
        print(f"The word was {word_to_guess.upper()}.")
        print("You lost.")
