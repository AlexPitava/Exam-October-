def sum_of_positive(nums):
    sum_positive = 0
    for num in nums:
        if num > 0:
            sum_positive += num
    return sum_positive