from mystery_word import word_guessed, is_letter_input

word_to_guess = 'racecar'


def test_word_guessed():
    assert not word_guessed(word_to_guess, [])
    assert not word_guessed(word_to_guess, ['r', 'c'])
    assert word_guessed(word_to_guess, ['r', 'e', 'a', 'c'])


def test_is_letter_input():
    assert is_letter_input("a")
    assert is_letter_input("Z")
    assert not is_letter_input("hello")
    assert not is_letter_input("")
    assert not is_letter_input("]")
