def clean_text(text):
    """Strip out every character that is not a letter."""
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    new_text = ""
    for char in text:
        if char in all_letters:
            new_text += char
    return new_text


def starts_with_letter(word, letter):
    return word[0].lower() == letter.lower()


def longest_word(sentence, starting_letter=None):
    """Returns the longest word in a sentence."""

    def is_valid(word):
        return starting_letter is None or starts_with_letter(
            word, starting_letter)

    words = sentence.split(" ")

    # Go through the list word by word
    current_longest = ""
    for word in words:
        word = clean_text(word)
        # If the current is longer than any word previously seen,
        # remember that word
        if is_valid(word) and len(word) > len(current_longest):
            current_longest = word

    return current_longest


print(
    longest_word(
        "This text has some words that are short; others are very long."))
print(
    longest_word(
        "This text has some words that are short; others are very long.",
        starting_letter="t"))
