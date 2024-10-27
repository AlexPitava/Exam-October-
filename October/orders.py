def order_str(s):
    if not s:
        return ""
    
    words = s.split()

    words.sort(key=lambda x: (-ord(x), x))
    
    return ''.join(words)
    
print(order_str("is2 Thi1s T4est 3a"))