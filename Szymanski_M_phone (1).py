## Matthew Szymanski
## 3/19/19
## CSCD 110
## Lemelin


# define main function to hold lists
LAST = 1
FIRST = 2
PHONE = 3
QUIT = 0
def displayMenu():
    print("Please choose from the following options:")
    print("1. Look up by last name")
    print("2. Look up by first name")
    print("3. Look up by phone number")
    print("0. QUIT")
        
            
def main():
    # first open file for reading
    myFile = open('entries.txt','r')

    # create lists
    lName = []
    fName = []
    phone = []
    count = 1 # keeps track of the lines in the file

    for line in myFile:
        line = line.strip()
        line = line.lower()
        
        if count % 3 == 1: # this formula gets last name
            lName.append(line)
        elif count % 3 == 2: # this formula gets first name
            fName.append(line)
        else:
            phone.append(line)
        count += 1 # keeps track of lines
    choice = 7
    while choice != 0:
        displayMenu()
        choice = int(input("Enter a choice: "))
        if choice == 1:
            looklast(lName, fName, phone)
        elif choice == 2:
            lookfirst(lName, fName, phone)
        elif choice == 3:
            lookphone(lName, fName, phone)

            # do the phone look up
        elif choice == QUIT:
            print("Thanks for using this program")
        else:
            print("Enter a valid menu choice")


    myFile.close()
    
def looklast(lName, fName, phone): # looklast function for if user inputs last name
    name = input("Enter the last name you would like to look up: ")
    name = name.lower()
    pointer = 0
    if name in lName:
        while True:
            try:
                pointer = lName.index(name,pointer)
                print(lName[pointer].title())
                print(fName[pointer].title())
                print(phone[pointer])
                pointer += 1
            except:
                break
    else:
        print("No entry can be found for", name)

def lookfirst(lName, fName, phone): # lookfirst function for if user inputs first name
    name = input("Enter the first name you would like to look up: ")
    name = name.lower()
    pointer = 0
    if name in fName:
        while True:
            try:
                pointer = fName.index(name,pointer)
                print(lName[pointer].title())
                print(fName[pointer].title())
                print(phone[pointer])
                pointer += 1
            except:
                break
    else:
        print("No entry can be found for", name)

def lookphone(lName, fName, phone): # lookphone function for if user inputs phone
    name = input("Enter the phone number you would like to look up: ")
    name = name.lower()
    pointer = 0
    if name in phone:
        while True:
            try:
                pointer = phone.index(name,pointer)
                print(lName[pointer].title())
                print(fName[pointer].title())
                print(phone[pointer])
                pointer += 1
            except:
                break
    else:
        print("No entry can be found for", name)

main()


    

    
