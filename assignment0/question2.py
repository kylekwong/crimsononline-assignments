# Kyle Kwong
# Question 2

def swapchars(string):
	# Initialize most and least common chars.
	mc_char, lc_char = string[0], string[0]

	# Make string into a list to modify later.
	s = list(string)

	# Set range for iterating over string as a list.
	y = range(0, len(string))

	# Initialize number of times most/least common letters appear.
	b, d = string.count(mc_char), string.count(lc_char)

	# Find most common and least common chars.
	for c in string:

		# Check that the character is a letter.
		if c.isalpha():

			# Calculate number of times current letter appears.
			a = string.count(c)

			# Check and swap if current char appears more/less
			# than current mc_char or lc_char respectively.
			# If current char appears equally with either mc_char
			# or lc_char, switch if alphabetically before either.
			if a > b:
				mc_char = c
				b = string.count(mc_char)
			elif (a == b) & (c.lower() < mc_char.lower()):
				mc_char = c
				b = string.count(mc_char)
			elif a < d:
				lc_char = c
				d = string.count(lc_char)
			elif (a == d) & (c.lower() < lc_char.lower()):
				lc_char = c
				d = string.count(lc_char)

	# Swap most common char with least common char
	# and vice-versa in list
	for x in y:
		if s[x] == mc_char:
			s[x] = lc_char
		elif s[x] == lc_char:
			s[x] = mc_char

	# Join list together
	mod_string = "".join(s)

	# Return modified string
	return mod_string