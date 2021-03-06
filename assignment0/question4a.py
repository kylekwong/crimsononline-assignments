# Kyle Kwong
# Question 4a

def look_away(num):
	# Import random for use later.
	import random	

	# Initialize some variables
	mario, wario, peach = True, True, True
	lives, wins, trials = 5, 0, num

	
	# Run trials number of trials
	while num > 0:

		# Re-initialize mario, wario, peach, and lives each trial.
		mario, wario, peach = True, True, True
		lives = 5

		# Keep playing game until lives run out (in current trial)
		# or if mario, wario, and peach lose.
		while lives > 0:

			# Generate random number 0 - 4.  0 forward, 1-4 represent the rest
			a = random.randint(0, 4)
			if a == 0:
				mario = False
			a = random.randint(0, 4)
			if a == 0:
				wario = False
			a = random.randint(0, 4)
			if a == 0:
				peach = False

			# Decrement lives each round
			lives -= 1

		# If luigi wins, increment wins.
		if (mario == False) & (wario == False) & (peach == False):
			wins += 1

		# Decrement number of trials left to do
		num -= 1

	# Calculate fraction of wins
	fraction = float(wins)/float(trials)

	#return number of wins
	return fraction