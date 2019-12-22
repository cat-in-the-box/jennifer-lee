#Tip Calculator - Minimum Wage
#Goal to calculate how much tip/hr a server needs to receive to live

##Variables
#Tip percentage for input, bill amount for input, minimum wage in NYC, living wage in NYC
tip_percentage = 0
bill_amount = 0
tip_amount = 0
minimum_tip = 0 #The minimum wage in NYC is 10.75. Customers have to average 32% tip

##Inputs
#User inputs the bill amount
bill_amount  = input("How much is your bill? ")
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
minimum_tip = round((int(bill_amount) * (33/100)), 2)

#Output
#Maintaining minimum wage based on user tip input and service
if (service == "Good" and float(tip_percentage) > 33 or service == "good" and float(tip_percentage) > 33 or service == "Average" and float(tip_percentage) > 33 or service == "average" and float(tip_percentage) > 33 or service == "Bad" and float(tip_percentage) > 33 or service == "bad" and float(tip_percentage) > 33) :
    print("Your tip is $", tip_amount , "! That's $", round((tip_amount - minimum_tip),2), "higher than the average tip!" )
elif (service == "Good" and float(tip_percentage) == 33 or service == "good" and float(tip_percentage) == 33 or service == "Average" and float(tip_percentage) == 33 or service == "average" and float(tip_percentage) == 33 or service == "Bad" and float(tip_percentage) == 33 or service == "bad" and float(tip_percentage) == 33) :
    print("You gave $", tip_amount , "in tips. That's the minimum wage tip!")    
elif (service == "Good" and float(tip_percentage) < 33 or service == "good" and float(tip_percentage) < 33 or service == "Average" and float(tip_percentage) < 33 or service == "average" and float(tip_percentage) < 33 or service == "Bad" and float(tip_percentage) < 33 or service == "bad" and float(tip_percentage) < 33) :
    print("You gave $", tip_amount , "in tips. That's $", abs(round((tip_amount - minimum_tip),2)), "lower than the average tip. You should give $", minimum_tip, "to meet the minimum wage.")
else:
    print("That was a lousy tip! The minumum wage in NYC is $10.75/hr. You need to tip higher.")
    