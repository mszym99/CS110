# create main fuction to hold list
def main():
    number_list =[]
    x = 1
    while x <= 10:
        # get numbers for the list
        num = float(input("Enter a number for the list: "))
        number_list.append(num)
        x += 1
    # print the list
    print(number_list)
    # print the low
    print("Low:", min(number_list))
    # print the max
    print("Max:", max(number_list))
    # identify total and average 
    total = 0
    for num in number_list:
        total += num
    average = total / len(number_list)
    print("Sum:", total)
    print("Average:", average)
    


main()
