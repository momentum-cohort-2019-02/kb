from mystery_word import word_guessed, is_letter_input, get_display_word

word_to_guess = 'racecar'


def test_word_guessed():
    assert not word_guessed(word_to_guess, [])
    assert not word_guessed(word_to_guess, ['r', 'c'])
    assert word_guessed(word_to_guess, ['r', 'e', 'a', 'c'])
    assert word_guessed("cattail", ['c', 't', 'a', 'l', 'm', 'i'])


def test_is_letter_input():
    assert is_letter_input("a")
    assert is_letter_input("Z")
    assert not is_letter_input("hello")
    assert not is_letter_input("")
    assert not is_letter_input("]")


def test_get_display_word():
    assert get_display_word("racecar", []) == "_ _ _ _ _ _ _"
    assert get_display_word("racecar", ['a', 'c']) == "_ A C _ C A _"
    assert get_display_word("racecar", ['a', 'c', 'r', 'e']) == "R A C E C A R"
    assert get_display_word("racecar", ['h', 'i', 'j']) == "_ _ _ _ _ _ _"
    assert get_display_word("racecar", ['h', 'i', 'j', 'c']) == "_ _ C _ C _ _"
