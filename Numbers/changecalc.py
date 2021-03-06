# This program will take a cost and the amount of money given and return the 
# amount of change broken down by denomination

# List of denominations in AUD currency
denominations = [100,50,20,10,5,2,1,0.5,0.2,0.1,0.05]

def get_required_input(prompt,desired_type,failure_message="Invalid input"):
	user_input = input(prompt)
	try:
		desired_type(user_input)
	except:
		print(failure_message)
		return False
	return user_input

# Init required variables
cost = False
cash = False
changeBreakdown = {}

# Returns the amount of change given the cost and amount of money given
def calculateChange(cost,cash):
	return abs(cost - cash)

# Returns a dict of the denominations and the quantity of each 
def findBestDenomination(change):
	changeLeft = change
	for d in denominations:
		denomCount = int(changeLeft / d)
		if denomCount > 0:
			changeBreakdown[d]  = denomCount
			changeLeft = changeLeft - (denomCount * d)
	return changeBreakdown

# Prints the denomination breakdown in a user friendly format
def printChangeBreakdown(changeBreakdown):
	for denom in denominations:
		if denom in changeBreakdown:
			print("$%s x %d" % (str(format(denom, ".2f")),changeBreakdown[denom]))

if __name__ == "__main__":
	while cost == False:
		cost = get_required_input("Enter the cost: $",float,"That is not a valid number.")

	while cash == False:
		cash = get_required_input("Enter the amount of cash given: $",float,"That is not a valid number")


	printChangeBreakdown(findBestDenomination(calculateChange(cost,cash)))
