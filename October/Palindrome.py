def palindrome(s):
    empty_string = ""

    for char in s.lower():
        if char.isalnum():
            empty_string += char

    return empty_string == empty_string[::-1]
