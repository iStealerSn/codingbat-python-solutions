# String-1 solutions
"""
Basic python string problems -- no loops. 
Use + to combine strings, len(str) is the number of chars in a String, 
str[i:j] extracts the substring starting at index i and running up to but not including index j.
"""

# hello_name
""" Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
For example: hello_name('Bob') → 'Hello Bob!' """

def hello_name(name): # Solution
      return 'Hello ' + name + '!'


# make_abba 
""" Given two strings, a and b, return the result of putting them together in the order abba, 
e.g. "Hi" and "Bye" returns "HiByeByeHi"."""

def make_abba(a, b): # Solution
  return a + b + b + a


# make_tags
""" The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, 
create the HTML string with tags around the word, e.g. "<i>Yay</i>"."""

def make_tags(tag, word): # Solution
  return '<' + tag + '>' + word + '</' + tag + '>'


# make_out_word
""" Given an "out" string length 4, such as "<<>>", and a word, 
return a new string where the word is in the middle of the out string, 
e.g. "<<word>>"."""

def make_out_word(out, word): # Solution
  return out[0] + out[1] + word + out[2] + out[3]


# extra_end 
""" Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
The string length will be at least 2. For example: extra_end('Hello') → 'lololo' """

def extra_end(str): # Solution
    return str[-2:] * 3


# first_two
""" Given a string, return the string made of its first two chars, so the String "Hello" yields 
"He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and 
the empty string "" yields the empty string "". For example - first_two('Hello') → 'He'
"""

def first_two(str): # Solution
    return str[0:2:]


# first_half 
""" Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
For example - first_half('WooHoo') → 'Woo'"""

def first_half(str): # Solution
    mist = len(str) / 2
    return str[:int(mist)]


# without_end
""" Given a string, return a version without the first and last char, so "Hello" yields "ell". 
The string length will be at least 2. For example - without_end('Hello') → 'ell' """

def without_end(str): # Solution
      return str[1:len(str)-1]


# combo_string
""" Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).
For example - combo_string('Hello', 'hi') → 'hiHellohi' """

def combo_string(a, b): # Solution
  return a + b + a if len(a) < len(b) else b + a + b


# non_start 
""" Given 2 strings, return their concatenation, except omit the first char of each. 
The strings will be at least length 1. For example - non_start('Hello', 'There') → 'ellohere' """

def non_start(a, b): # Solution
  return a[1:] + b[1:]


# left2
""" Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
The string length will be at least 2. For example - left2('Hello') → 'lloHe'"""

def left2(str): # Solution
  return str[2:] + str[:2]


# Thank you for looking up my solution hope it has been helpful.