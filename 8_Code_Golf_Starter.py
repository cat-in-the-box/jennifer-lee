'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.


sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''

def sleep_in(weekday, vacation):
    return True if weekday == False and vacation == False or weekday == False and vacation == True or weekday == True and vacation == True else False

'''
Given three ints, a b c, return True if b is greater than a, and c is greater than b.
However, with the exception that if "bOk" is True, b does not need to be greater than a.


in_order(1, 2, 4, False) → True
in_order(1, 2, 1, False) → False
in_order(1, 1, 2, True) → True
'''

def in_order(a, b, c, bOk):
    return True if int(a < b) == True and int(b < c) == True and bOk == False or int(b < c) == True and bOk == True else False

'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.


extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
'''

def extra_end(str):
    newstr = str[-2:]
    print(newstr*3)

'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
'''

def make_chocolate(small, big, goal):
    small_bars = int(goal % (big * 5))
    return (small_bars) if small == small_bars else (-1)

'''
HINT FOR LIST PROBLEMS: Use a[0], a[1], ... to access elements in a list, len(a) is the length.

Given a list of ints, return True if 6 appears as either the first or last element in the list.
The list will be length 1 or more.


first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
'''
def first_last6(nums):
    return True if nums[0] == 6 or nums[-1] == 6 else False

'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.


rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''

def rotate_left3(nums):
    new_nums = nums
    first_num = new_nums[0]
    new_nums.pop(0)
    new_nums.append(first_num)
    return new_nums

'''
Return the number of even ints in the given list.
Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.


count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

"Option 1"
def count_evens(nums):
    even_list = []
    
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return len(even_list)

"Option 2"

def count_evens(nums):
    count = 0
    
    for n in nums:
        if n % 2 == 0:
            count = count + 1
    return count

'''
Given a list length 1 or more of ints, return the difference between the largest and smallest values in the list.
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.


big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
'''
def big_diff(nums):
#make smaillest and largest variable
    s = nums[0]
    l = nums[0]
#if assign largest and smallest number to s/l variable
    for n in nums:
        if n < s:
            s = n
        elif n > l:
            l = n
        return l - s
        

# Call functions here
red = sleep_in(True, True)
print(red)
green = in_order(2, 1, 3, True)
print(green)
extra_end("Hello")
blue = make_chocolate(2, 2, 12)
print(blue)
orange = first_last6([1, 2, 6, 7, 3, 5, 2, 6])
print(orange)
purple = rotate_left3([4,5,6])
print(purple)