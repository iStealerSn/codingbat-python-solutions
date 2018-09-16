# String-2 solution
"""
Medium python string problems -- 1 loop..
Use + to combine strings, len(str) is the number of chars in a String, str[i:j]
extracts the substring starting at index i and running up to but not including index j.
"""

# double_char
"""
Given a string, return a string where for every char in the original, there are two chars.
For example - double_char('The') → 'TThhee'
"""

def double_char(str):
    double = ''
    for char in str:
        double += char * 2

    return double


# count_hi
"""
Return the number of times that the string "hi" appears anywhere in the given string.
For example - count_hi('abc hi ho') → 1
"""

def count_hi(str):
  return str.count('hi')


# cat_dog
"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
For example - cat_dog('catdog') → True
"""

def cat_dog(str):
  return (str.count('cat') == str.count('dog'))


# count_code
"""
Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.
For example - count_code('aaacodebbb') → 1
"""

def count_code(str):
  count = 0
  i = 0
  while "co" in str[i:]:
    if len(str[i+str[i:].index("co"):]) >= 4 and str[i+3+str[i:].index("co")] == "e":
      count += 1
    i += str[i:].index("co")+3
  return count


# end_other
"""
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.
For example - end_other('Hiabc', 'abc') → True
"""

def end_other(a, b):
  long_,short_ = (a,b) if len(a) > len(b) else (b,a)
  return long_.lower().endswith(short_.lower())


# xyz_there
"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly 
preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
For example - xyz_there('abcxyz') → True
"""

def xyz_there(str):
    index = 0

    while 'xyz' in str[index:]:
        if str[index - 1 + str[index:].index('xyz')] != '.':
            return True
        index += str[index:].index('xyz') + 2
    return False

# Thank you for looking up my solution