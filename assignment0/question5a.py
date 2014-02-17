# Kyle Kwong
# Question 5

def shuttles():

	# Import urllib and json modules
	import urllib, json, datetime

	# Open URL with data
	shuttle_url = urllib.urlopen("http://shuttleboy.cs50.net/api/1.2/trips?a=Quad&b=Mass+Ave+Garden+St&output=json")

	# Get data from URL
	data = json.loads(shuttle_url.read())

	# Initialize earliest three shuttles
	shuttle1, shuttle2, shuttle3 = data[0], data[1], data[2]

	# Calculate difference between shuttle times and now
	time1 = datetime.datetime.strptime(shuttle1["departs"], "%Y-%m-%dT%H:%M:%S")
	time2 = datetime.datetime.strptime(shuttle2["departs"], "%Y-%m-%dT%H:%M:%S")
	time3 = datetime.datetime.strptime(shuttle3["departs"], "%Y-%m-%dT%H:%M:%S")
	diff1 = float(datetime.timedelta.total_seconds(time1 - datetime.datetime.now())) / 60.
	diff2 = float(datetime.timedelta.total_seconds(time2 - datetime.datetime.now())) / 60.
	diff3 = float(datetime.timedelta.total_seconds(time3 - datetime.datetime.now())) / 60.

	# Parse string of shuttle time for printing
	str_time1 = shuttle1["departs"].split("T")
	str_time2 = shuttle2["departs"].split("T")
	str_time3 = shuttle3["departs"].split("T")

	# Print out results
	print "The next shuttle comes at %s, which is in %.2f minutes." % (str_time1[1], diff1)
	print "After, the next shuttle comes at %s, which is in %.2f minutes." % (str_time2[1], diff2)
	print "After that, the next shuttle comes at %s, which is in %.2f minutes." % (str_time3[1], diff3)