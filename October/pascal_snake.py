def pascal_to_snake(s):
    result = ""
    for char in s:
        if char.isupper() and result:
            result += "_"
        result += char.lower()
    return result.replace(" ", "_")