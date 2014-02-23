# Kyle Kwong
# Question 4b

# Calculate probability of one character facing forward
# at least once.
f_once = 1. - (4./5.) ** 5.

# Calculate probability of all three characters facing forward
# at least once (luigi winning)
win = f_once ** 3.

print win