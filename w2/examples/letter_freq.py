example_string = "ksdgflp09erwlcv,mbqiex cfs;nfqpy3 23f3r[k"


def unique_chars(a_str):
    """Given a string, get all the unique characters."""
    seen_chars = []
    for char in a_str:
        if char not in seen_chars:
            seen_chars.append(char)
    return seen_chars


def char_freq(a_str):
    """Given a string, get the frequency 
    of each character in the string."""
    char_count = {}
    for char in a_str:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

    return char_count


print(" ".join(unique_chars(example_string)))
char_count = char_freq(example_string)
print(char_count)
