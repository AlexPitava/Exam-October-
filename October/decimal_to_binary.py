def decimal_to_binary(decimal):
    try:
        decimal = int(decimal)
        binary_str = bin(decimal)[2:]
        return binary_str
    except ValueError:
        return "Error: Input must be a valid integer."     