"""
Execise 10
"""


def find_and_replace(text, old_str, new_str):
    """
    Find and replace all occurrences of a substring in a given text.

    This code defines a function called find_and_replace that takes three arguments:
    text (the original text), old_str (the substring to be replaced),
    and new_str (the substring to replace the old_str).

    The function iterates through the text character by character and checks
    if the current substring matches the old_str. If it does,
    it appends the new_str to the replaced_str and moves the index i forward by
    the length of old_str. If it doesn't match, it appends the current character
    to the replaced_str and moves the index i forward by 1.

    Finally, the function returns the modified replaced_str with all occurrences of
    old_str replaced with new_str.

    Args:
        text (str): The original text.
        old_str (str): The substring to be replaced.
        new_str (str): The substring to replace the old_str.

    Returns:
        str: The modified text with all occurrences of old_str replaced with new_str.
    """
    # FIX : complete this
    i = 0
    while i < text.__len__():
        if text[i:i+old_str.__len__()] == old_str:
            text = text[:i] + new_str + text[i+old_str.__len__():]
            i += 1
        else:
            i += 1
    return text
