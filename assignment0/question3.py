# Kyle Kwong
# Question 3

def concat (num, *args):
	# Convert arg tuple to a sorted list.
	str_list = map(str, list(args))
	str_list.sort(key=len, reverse=True)

	# Initialize the return string.
	string = ""

	# Concat strings depending on the number given.
	if num == -1:
		for c in str_list:
			string += c
	else:
		counter = 0
		for c in str_list:
			if counter < num:
				string += c
				counter += 1

	# Return string
	return string