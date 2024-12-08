def longest_consecutive(nums):
    if not nums: #თუ ცარიელია მაშინ დააბრუნებს 0-ს
        return 0
    
    nums_set = set(nums)
    longest = 0
    
    for num in nums_set:
        if num - 1 not in nums_set: #ვამოწმებთ იწყება თუ არა აქედან თანმიმდევრობა
            current_num = num
            current_length = 1
            
            while current_num + 1 in nums_set: # ვნახულობთ იმ ელემენტების რაოდენობას რომლებიც თანმიმდევრულად მიმდინარეობს
                current_num += 1
                current_length += 1
            
            longest = max(longest, current_length)

    return longest 
