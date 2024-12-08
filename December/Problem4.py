def longest_unique_substring(x):
    substring = ""
    max_length = 0

    for char in x:
        if char in substring:
            # remove duplictes
            substring = substring[substring.index(char) + 1:]
        substring += char # add char to substring
        max_length = max(max_length, len(substring)) # to update max_length if new max_length found

    return max_length
