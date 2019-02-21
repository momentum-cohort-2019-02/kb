import string


def remove_non_letters(text):
    """Strip out every character that is not a letter."""
    all_letters = string.ascii_letters

    new_text = ""
    for char in text:
        if char in all_letters:
            new_text += char
    return new_text


def normalize_text(text):
    """
    Given a text, lowercases it, removes all punctuation, 
    and replaces all whitespace with normal spaces. Multiple whitespace will
    be compressed into a single space.
    """
    text = text.casefold()
    valid_chars = string.ascii_letters + string.whitespace + string.digits

    # Remove all punctuation
    new_text = ""
    for char in text:
        if char in valid_chars:
            new_text += char

    text = new_text
    text = text.replace("\n", " ")
    return text
