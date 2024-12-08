from math import floor #floor ამრგვალებს რიცხვს უახლოეს ინტეჯერამდე მხოლოდ ქვევით, 4.8 გახდება 4 და არა 5.
def sum_positive_floor(nums):
    sum = 0
    for num in nums:
        if num > 0:
            sum += floor(num)
    return sum