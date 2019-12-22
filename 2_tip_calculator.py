#Tip calculator static
#Goal: Calculate and print out the tip from a bill

#Variables
#Need one for the tip percentage (static) and one for the bill amount
tip_percentage = float(0.185)
bill_amount = 0

#Inputs
#Need user to define how much the bill is
bill_amount = float(input("How much is the bill? "))
print ("The bill is ", float(bill_amount), " dollars")

#Calculation
#Tip should be bill x tip percentage
print ("The tip amount is ", bill_amount * tip_percentage)
