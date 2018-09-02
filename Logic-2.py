# Logic 2

""" Medium boolean logic puzzles -- if else and or not"""


# make_bricks 
"""" We want to make a row of bricks that is goal inches long. 
We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
Return True if it is possible to make the goal by choosing from the given bricks. 
This is a little harder than it looks and can be done without any loops.
For example - make_bricks(3, 1, 8) → True"""

def make_bricks(small, big, goal):
    resto = goal
    resto -= 5*min(big,goal/5)
    return resto-small <= 0


# lone_sum
""" Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, it does not count towards the sum.
For example - lone_sum(1, 2, 3) → 6"""

def lone_sum(a, b, c): # Solution A
    if a==b and b==c and a==c:
        return 0
    elif a==b:
        return c
    elif b==c:
        return a
    elif a==c:
        return b
    else:
        return sum((a,b,c))

def _lone_sum(a, b, c): # Solution B
    sum = 0
  
    sum += a if not a in [b,c] else 0
    sum += b if not b in [a,c] else 0
    sum += c if not c in [a,b] else 0
  
    return sum


# lucky_sum
""" Given 3 int values, a b c, return their sum.
However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. 
So for example, if b is 13, then both b and c do not count.
For example - lucky_sum(1, 2, 3) → 6 """

def lucky_sum(a, b, c): # Solution A
    sum_ = 0
  
    if a==13:
        sum_
    elif b==13:
        sum_ += a
    elif c==13: 
        sum_ = a+b
    else:
        sum_ = a+b+c
  
    return sum_


def _lucky_sum(a, b, c): #Solution B
    result_ = [a,b,c,13]
    res = 0 
  
    for i in result_[:result_.index(13)]:
        res += i
  
    return res


#no_teen_sum
""" Given 3 int values, a b c, return their sum. 
However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, 
except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"
that takes in an int value and returns that value fixed for the teen rule. 
In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). 
Define the helper below and at the same indent level as the main no_teen_sum().
For example - no_teen_sum(1, 2, 3) → 6"""

def no_teen_sum(a, b, c):
    sum_ = fix_teen(a) + fix_teen(b) + fix_teen(c)
    return sum_


def fix_teen(n):
    return n if n not in [13, 14, 17, 18, 19] else 0


# round_sum
"""For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, 
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, 
write a separate helper "def round10(num):" and call it 3 times. 
Write the helper entirely below and at the same indent level as round_sum().
For example - round_sum(16, 17, 18) → 60
"""

def round_sum(a, b, c):
    return round10(a)+round10(b)+round10(c)

def round10(num):
    return (num+5)/10*10


# close_far
"""Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 
1), while the other is "far", differing from both other values by 2 or more. 
Note: abs(num) computes the absolute value of a number.
For example - close_far(1, 2, 10) → True
"""

def close_far(a, b, c):
  return (abs(abs(b)-abs(c))>=2) and \
  ((abs(abs(b)-abs(a))<=1 and abs(abs(c)-abs(a))>=2) \
  or (abs(abs(c)-abs(a))<=1 and abs(abs(b)-abs(a))>=2))