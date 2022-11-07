# Matthew Szymanski, Intro to programming, 2/5/19, Assignment 2
# Variables
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

# Prompt the user to enter a number
while True:

    number = int(input("Please enter a number between 1-7: "))
    if number == 1:
        print("Monday")
    elif number == 2:
        print("Tuesday")
    elif number == 3:
        print("Wednesday")
    elif number == 4:
        print("Thursday")
    elif number == 5:
        print("Friday")
    elif number == 6:
        print("Saturday")

        print("HAPPY WEEKEND!")
    elif number == 7:
        print("Sunday")

        print("HAPPY WEEKEND!")
    else:
        print("ERROR")
        

