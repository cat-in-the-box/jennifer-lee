#Tip Calculator - Living Wage
#Goal to calculate how much tip/hr a server needs to receive to live in NYC

##Variables
#Tip percentage for input, bill amount for input, minimum wage in NYC
tip_percentage = 0
bill_amount = 0
tip_amount = 0
living_tip = 0 #The minimum wage in NYC is 14.30. Customers have to average 43% tip
extra_tip = 0

##Inputs
#User inputs the bill amount
bill_amount = input("How much is your bill? ")
if (bill_amount.isdigit()) :
    pass
else:
    print ("Please input a number")

#User inputs the quality of service
service = input("How was your service? Good/Average/Bad: ")
if (service == "Good" or service == "good") :
    pass
elif (service == "Average" or service == "average") :
    pass
elif (service == "Bad" or service == "bad") :
    pass
else:
    print ("Please respond with Good, Average, or Bad")

#User inputs the dollar amount they want to tip off their bill
tip_percentage = input("What percentage do you want to tip? Please enter an integer ")
if (tip_percentage.isdigit()) :
    pass
else:
    print ("Please input a number") 

##Calculation
#Tip percentage should be tip amount / bill 
tip_amount = round((int(bill_amount) * (int(tip_percentage) / 100)),2)
living_tip = round((int(bill_amount) * (43/100)), 2)
extra_tip = round((int(bill_amount) * (15/100)), 2)
print (tip_amount)
print (living_tip)
print (extra_tip)

#Output
#Maintaining living wage based on user tip input and service, receiving extra tip for good service
if (service == "Good" and float(tip_percentage) > 43 or service == "good" and float(tip_percentage) > 43 or service == "Average" and float(tip_percentage) > 43 or service == "average" and float(tip_percentage) > 43 or service == "Bad" and float(tip_percentage) > 43 or service == "bad" and float(tip_percentage) > 43) :
    print("Your tip is $", tip_amount , "! That's $", round((tip_amount - living_tip),2), "higher than the average living wage tip!" )
elif (service == "Good" and float(tip_percentage) == 43 or service == "Good" and float(tip_percentage) == 43 ) :
    print("You gave $", tip_amount , "in tips. That's the minimum living wage tip! You should give, $", extra_tip, "on top for good service.")    
elif (service == "Average" and float(tip_percentage) == 43 or service == "average" and float(tip_percentage) == 43 or service == "Bad" and float(tip_percentage) == 43 or service == "bad" and float(tip_percentage) == 43) :
    print("You gave $", tip_amount , "in tips. That's the minimum living wage tip!")    
elif (service == "Good" and float(tip_percentage) < 43 or service == "good" and float(tip_percentage) < 43) :
    print("You gave $", tip_amount , "in tips. That's $", abs(round((tip_amount - living_tip),2)), "lower than the minimum living wage tip. You should give $", living_tip, "to meet the minimum living wage and $", extra_tip, "on top for good service.")
elif (service == "Average" and float(tip_percentage) < 43 or service == "average" and float(tip_percentage) < 43 or service == "Bad" and float(tip_percentage) < 43 or service == "bad" and float(tip_percentage) < 43) :
    print("You gave $", tip_amount , "in tips. That's $", abs(round((tip_amount - living_tip),2)), "lower than the minimum living wage tip. You should give $", living_tip, "to meet the minimum living wage.")
else:
    print("That was a lousy tip! The minumum living wage in NYC is $14.30/hr. You need to tip higher.")
