def find_missing(num):
    if len(num) == 1 or 0:
        return []
    n = len(num) + 1
    real = set(range(1, n + 1))
    nums = set(num)
    missing = real - nums
    return missing
    

