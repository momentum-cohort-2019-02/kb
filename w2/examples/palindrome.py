def is_palindrome(text):
    """Return True or False if the text is a palindrome."""
    text = remove_non_letters(text.lower())

    # i => -(i + 1)
    # 0 => -1
    # 1 => -2
    # 2 => -3
    for idx in range(len(text) // 2):
        # print(text, text[idx], text[-(idx + 1)])
        if text[idx] != text[-(idx + 1)]:
            return False

    return True


def is_palindrome_recursive(text):
    """Return True or False if the text is a palindrome."""
    text = remove_non_letters(text.lower())
    # print(text)

    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome_recursive(text[1:-1])


def is_palindrome_easy(text):
    """Return True or False if the text is a palindrome."""
    text = remove_non_letters(text.lower())
    return text == text[::-1]


def remove_non_letters(text):
    """Strip out every character that is not a letter."""
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    all_letters += all_letters.upper()

    # new_text = ""
    # for char in text:
    #     if char in all_letters:
    #         new_text += char
    # return new_text

    chars = []
    for char in text:
        if char in all_letters:
            chars.append(char)
    return "".join(chars)


text = input("Enter a possible palindrome: ")
if is_palindrome(text):
    print("is a palindrome")
else:
    print("is not a palindrome")
