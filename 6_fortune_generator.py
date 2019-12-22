#Load the random number generator
import random


#Random fortune teller 
fortune = ["Tomorrow you will sit on a pickle", "Someday, you will grow a moustache", "A small stranger will give you a Starburst", "Your holiday bush will smell like grapes"]
random_outcome = random.choice(fortune)
print (random_outcome)

#Semi-random fortune teller
#Input birth month
birth_month = input("What is your birth month?")
#select a random number
random_number = random.randint(1,12)
#if brith month matches random number, user gets jackpot fortune, otherwise they get a fortune based on their birth month
if (int(birth_month) == int(random_number)):
    print ("You will win the lottery!")
elif (int(birth_month) == 1):
    print ("You have a deep appreciation of the arts and music.")
elif (int(birth_month) == 2):
    print ("You will travel to many places.")
elif (int(birth_month) == 3):
    print ("Your emotional nature is strong and sensitive.")
elif (int(birth_month) == 4):
    print ("To one who waits, a moment seems a year.")
elif (int(birth_month) == 5):
    print ("Treat everyone as a friend.")    
elif (int(birth_month) == 6):
    print ("You will reach the height of success in whatever you do.")  
elif (int(birth_month) == 7):
    print ("Your venture will be a success.")  
elif (int(birth_month) == 8):
    print ("Now is the time to try something new.")  
elif (int(birth_month) == 9):
    print ("Don't let doubt and suspicion bar your progress.")
elif (int(birth_month) == 10):
    print ("You are careful & systematic in your business arrangements.")  
elif (int(birth_month) == 11):
    print ("You have an active mind and a keen imagination.")  
elif (int(birth_month) == 12):
    print ("You will reach the height of success in whatever you do.")  
else:
    print ("There's no way you could be born in that month!")