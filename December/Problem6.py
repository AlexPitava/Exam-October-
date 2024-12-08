def find_intersection(lst1, lst2):
    if not lst1 or not lst2:
        return []
    
    set1 = set(lst1)
    set2 = set(lst2)
    
    intersection = list(set1 & set2) #& გამოიყენება რათა ინტერსექცია(თანაკვეთა) ვნახოთ ორ ან მეტ ლისტს შორის.
    
    return intersection

print(find_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))