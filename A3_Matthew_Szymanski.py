'''Matthew Szymanski
   Lemelin
   2/26/19
   CSCD 110'''






# Define main variables that will be prompted to user to make a choice 1-6

def main():
    Count0to75 = 1
    Count3to129 = 2
    Addnum210to235 = 3
    PrintEvil = 4
    PrintInt = 5
    Quit = 6
    Extra = 7

# Display menu to allow user to choose options

    choice = 8

    while choice != 6:
        print("Please enter a menu choice: ")
        print("1. Count from 0 to 75 by 5's.")
        print("2. Count from 3 to 129 by 7's.")
        print("3. Add the numbers from 210 to 235.")
        print("4. Print the phrase Don't be evil. one letter per line.")
        print("5. Print the integers from 5 to 15.")
        print("6. Quit.")

# Get users number

        choice = int(input("Please enter a your number between 1-6: "))
        # If number is out of bounds
        if choice < 0 or choice > 7:
            print("Invalid number. Please enter an integer between 1-6.")
        if choice == Count0to75:
            x = 0
            count = 0
            while x < 75:
                x += 5
                print(x)
        if choice == Count3to129:
            x = 3
            count = 0
            while x < 129:
                x += 7
                print(x)
        if choice == Addnum210to235:
            count = 210
            x = 210
            while x < 235:
                x = x + 1
                count += x
                print(count)
            print("The summation of 210-235 is", count)
        if choice == PrintEvil:
            for char in "Don't be evil.":
                print(char)
        if choice == PrintInt:
            for i in range(5,16,5):
                print(i)
        if choice == Quit:
            break
        

        
            
            
                
main()
        
        
    
                 
