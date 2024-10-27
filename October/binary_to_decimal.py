def binary_to_decimal(binary_str):
    if all(char in "01" for char in binary_str):
        decimal = int(binary_str, 2)
        return decimal
    else:
        return "Error."