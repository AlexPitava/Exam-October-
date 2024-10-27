def remove_duplicates(lst):
    arr = []
    for i in lst:
        if i not in arr:
            arr.append(i)
    return arr

