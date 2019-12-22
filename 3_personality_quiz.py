#Quiz: Which Pokemon are you? Users will be asked a series of yes/no questions to determine which Pokemon they are

#Variables - define Pokemon
charmander = 0
jigglypuff = 0
snorelax = 0
bulbasaur = 0

#Questions - ask user yes or not to award a point to each variable
q1 = input("Do you like spicy food? Yes or No: ")
if (q1 == "Yes") or (q1 == "yes"):
    charmander = +1
else:
    charmander = 0
    

q2 = input("Do you enjoy karaoke? Yes or No: ")
if (q2 == "Yes") or (q2 == "yes"):
    jigglypuff = +2
else:
    jigglypuff = 0
    
q3 = input("Do you sleep for more than 12 hours on the weekend? Yes or No: ")
if (q3 == "Yes") or (q3 == "yes"):
    snorelax = +3
else:
    snorelax = 0
    
q4 = input ("Do you like to garden? Yes or No: ")
if (q4 == "Yes") or (q4 == "yes"):
    bulbasaur = +4
else:
    bulbasaur = 0

#Determine the Pokemone Type the user is

if (charmander > jigglypuff) and (charmander > snorelax) and (charmander > bulbasaur):
    print ("Congrats! You're a Charmander")
elif (jigglypuff > charmander ) and (jigglypuff > snorelax) and (jigglypuff > bulbasaur):
    print ("Congrats! You're a Jigglypuff")
elif (snorelax > charmander ) and (snorelax > jigglypuff) and (snorelax > bulbasaur):
    print ("Congrats! You're a Snorelax")
elif (bulbasaur > charmander ) and (bulbasaur > jigglypuff) and (bulbasaur > snorelax):
    print ("Congrats! You're a Bulbasaur")
else:
    print ("Hooray! You're a Pikachu")