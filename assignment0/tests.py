# Kyle Kwong
# tests.py

# Import pprint for formatting
from pprint import pprint

# Import functions from assignments for testing
from question1 import fizzbuzz
from question2 import swapchars
from question3 import concat
from question4a import look_away
from question5a import shuttles

# Testing question 1.
print "==testing question 1=="

# Expected output: Numbers 1 through 100, except every multiple of 3, 5, and 15
# are replaced with Fizz, Buzz, and FizzBuzz respectively.
fizzbuzz()

print
print 

# Testing question 2.
# Expected output: 
print "==testing question 2=="

# Expected output: "Thcrc wcrc a lot of cseopcoplcs in thc clcvator on Tucsday."
pprint(swapchars("There were a lot of escopeoples in the elevator on Tuesday."))

# Expected output: "ihhhhhh"
pprint(swapchars("hiiiiii"))

print
print

# Testing question 3
print "==testing question 3=="

# Expected output: 'awesome'
pprint(concat(1, "Kyle", "is", "awesome"))

# Expected output: 'what???2345'
pprint(concat(-1, "what", "???", 5, 234))

# Expected output: ''
pprint(concat(0, "kyle", "kyle", "kyle"))

# Expected output: 'abcbcc'
pprint(concat(3, 'bc', 'c', 'abc'))

print
print

# Testing question 4a
print "==testing question 4a=="

#Expected output: Should be close to 0.6547, as calculated in question 4b
pprint(look_away(10000))
pprint(look_away(10000))
pprint(look_away(10000))
pprint(look_away(10000))
pprint(look_away(10000))

print
print

print "==testing question 5a=="

# Expected output: Varies depending on time used
shuttles()

print