# Kyle Kwong
# Question 1

# Counting numbers 1 - 100
def fizzbuzz():
	for x in range (1, 101):

		# Check for multiples of 15 (divisible by 5 and 3),
		# then multiples of only 5, then multiples of only 3.
		# Print all other values as they are.
		if x % 15 == 0: 
			print "FizzBuzz"
		elif x % 5 == 0:
			print "Buzz"
		elif x % 3 == 0:
			print "Fizz"
		else:
			print x