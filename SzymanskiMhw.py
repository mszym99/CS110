# Declare your constant variables
FEET = 1
METERS= 2
FAHRENHEIT = 3
CELSIUS = 4
QUIT = 0

# We will have a main function
def main():
    choice = 7
    while choice != QUIT:
        display_menu() # We call our display menu function
        choice = int(input("Enter your choice: "))
        # First option
        if choice == FEET:
            feet = float(input("Enter your length in feet to convert to meters: "))
            print(feet, "feet is equal to", format(convert_to_meters(feet),'.2f'),"meters.")
        # Second option
        elif choice == METERS:
            meters = float(input("Enter your length in meters to convert to feet: "))
            print(meters, "meters is equal to", format(convert_to_feet(meters),'.2f'),"feet.")
        # Third option
        elif choice == FAHRENHEIT:
            fahrenheit = float(input("Enter your temperature in fahrenheit to convert to celsius: "))
            print(fahrenheit, "degrees fahrenheit is equal to", format(convert_to_celsius(fahrenheit),'.2f'),"degrees celsius.")
        # Fourth option    
        elif choice == CELSIUS:
            celsius = float(input("Enter your temperature in celsius to convert to fahrenheit: "))
            print(celsius, "degrees celsius is equal to", format(convert_to_fahrenheit(celsius),'.2f'),"degrees fahrenheit.")
        # Quit option
        elif choice == QUIT:
            print("You have quit.")
            break

# Define more functions            
def display_menu():
    

    print("Please enter a menu option")
    print("1. Convert feet to meters")
    print("2. Convert meters to feet")
    print("3. Convert fahrenheit to celsius")
    print("4. Convert celsius to fahrenheit")
    print("0. Quit")
def convert_to_meters(f):
    
    

    return f / 3.20808
def convert_to_feet(m):
    return m / .3048
def convert_to_celsius(F):
    return (F - 32) * 5/9
def convert_to_fahrenheit(C):
    return (C * 9/5) + 32

            
    
    
main()
