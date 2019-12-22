#Two as one
#Get three integers from the user and then tell the user whether two of them can add to make the third.

#Designate 
num1 = 0
num2 = 0
num3 = 0

num1 = input("Put in a number. This will be number 1: ")
num2 = input("Put in a second number. This will be number 2: ")
num3 = input("Put in a third number. This will be number 3: ")
if (int(num1) + int(num2) == int(num3)):
    print ("Number 1 and Number 3 add up to Number 3!")
elif (int(num2) + int(num3) == int(num1)):
    print ("Number 2 and Number 3 add up to Number 1!")
elif (int(num3) + int(num1) == int(num2)):
    print ("Number 1 and Number 3 add up to Number 2!")
else:
    print ("The numbers don't add up")