# List-2 solutions

"""
Medium python list problems -- 1 loop.. Use a[0], a[1], ... to access elements in a list, len(a) is the length.
"""

# count_evens
"""
Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
For example - count_evens([2, 1, 2, 3, 4]) → 3
"""

def count_evens(nums):
  count = 0
  for i in nums:
    if i % 2 == 0:
      count += 1
  return count


# big_diff
"""
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
For example - big_diff([10, 3, 5, 6]) → 7
"""

def big_diff(nums):
  return max(nums)-min(nums)


# centered_average
"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.
For example - centered_average([1, 2, 3, 4, 100]) → 3
"""

def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))
    return (sum((nums)) / len(nums))


# sum13
"""
Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.
For example - sum13([1, 2, 2, 1]) → 6
"""

def sum13(nums):
    while 13 in nums:
        if nums.index(13) < len(nums) - 1:
            nums.pop(nums.index(13) + 1)

        nums.pop(nums.index(13))

    return sum(nums)


# sum67
"""
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
For example - sum67([1, 2, 2]) → 5
"""

def sum67(nums):
    sum_ = 0
    position = False

    for n in nums:
        if n == 6:
            position = True
            continue
        if n == 7 and position:
            position = False
            continue
        if not position:
            sum_ += n

    return sum_


# has22
"""
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
For example - has22([1, 2, 2]) → True
"""

def has22(nums):
  found = False
  for i in range(0,len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      found = True
  return found


# Thank you for looking up my solution