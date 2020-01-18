def run_calculator():
    run_program = input("Which function would you like to run (pick A,B,C)? Your options are: \nA. add_numbers \nB. subtract_numbers \nC. average_numbers \nYou can also input 'Quit' if you don't want to play: ")
    if run_program == "A":
        print ("Okay, let's get started with add_numbers!")
        num1 = get_input()
        num2 = get_input()
        addition = add_numbers(num1, num2)
        print (addition)
    elif run_program == "B":
        print ("Okay, let's get started with subtract_numbers!")
        num1 = get_input()
        num2 = get_input()
        subtraction = subtract_numbers(num1, num2)
        print (subtraction)
    elif run_program == "C":
        print ("Okay, let's get started with average_numbers!")
        num1 = get_input()
        num2 = get_input()
        average = average_numbers(num1, num2)
        print (average)
    elif run_program == "Quit":
        quit()
    else:
        print ("Please select an option.")

def get_input():
    user_number = int(input("Please enter a number: "))
    return (user_number) #You will change this return when you write this function

def add_numbers(num1, num2):
    addition = num1 + num2
    return (addition)

def subtract_numbers(num1, num2):
    subtraction = num1 - num2
    return (subtraction)

def average_numbers(num1, num2):
    average = (num1 + num2)/2
    return (average)
    
run_calculator()
