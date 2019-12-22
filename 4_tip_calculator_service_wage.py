#Tip Calculator - Based on service
#Goal - calculate how much tip a server should receive based on service

##Variables
#Tip percentage for input, bill amount for input, minimum wage in NYC, living wage in NYC
tip_percentage = 0
bill_amount = 0
tip_amount = 0

##Inputs
#User inputs the bill amount
bill_amount  = input("How much is your bill? ")
#User inputs the quality of service
service = input("How was your service? Good/Average/Bad: ")

##Calculation
tip_percentage = (20/100)
print (tip_percentage)
tip_amount = float(bill_amount) * float(tip_percentage)
print (tip_amount)

#Output for tip based on standard of service 
if service == "Good" or service == "good" :
    tip_percentage = (20/100)
    tip_amount = round((float(bill_amount) * float(tip_percentage)),2)
    print("Your tip is $", tip_amount , "! That's a good tip for good service." )
elif service == "Average" or service == "average" :
    tip_percentage = (14/100)
    tip_amount = round((float(bill_amount) * float(tip_percentage)), 2)
    print("Your tip is $", tip_amount , "! That's a good tip for average service." )
elif service == "Bad" or service == "bad" :
    tip_percentage = (6/100)
    tip_amount = round((float(bill_amount) * float(tip_percentage)), 2)
    print("Your tip is $", tip_amount , "! That's a good tip for poor service." )
else:
    print("Please rate your service ")