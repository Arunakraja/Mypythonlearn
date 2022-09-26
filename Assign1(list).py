lst =[]
num = 5 #int(input('Enter number of number want : '))
for n in range(num):
    numbers = int(input('Enter the number :'))
    lst.append(numbers)
print("1.Reverse of list")
print("2.Maximum of number in list")
print("3.Minimum of number in list")
print("4.Sum of number in list")
print("5.Length of list")
print("6.second largest of list")
choice = int(input("enter the choice : "))
print("list of number is ",lst)
if choice ==1 :
    lst.reverse()
    print("reverse list of number is ", lst)
elif choice ==2 :
    print("maximum of number is ", max(lst))
elif choice ==3 :
    print("minimum of number is ",min(lst))
elif choice ==4 :
    print("Sum of number is ",sum(lst))
elif choice ==5:
    print("length of list is ",len(lst))
elif choice ==6 :
    temp = max(lst)
    lst.remove(temp)
    print(lst)
    print("The second maximum of list is ",max(lst))
go = int(input("If you want continue choice enter 1 or 0 :"))
while go != 0 :
        choice = int(input("enter the choice : "))
        print("list of number is ", lst)
        if choice == 1:
            lst.reverse()
            print("reverse list of number is ", lst)
        elif choice == 2:
            print("maximum of number is ", max(lst))
        elif choice == 3:
            print("minimum of number is ", min(lst))
        elif choice == 4:
            print("Sum of number is ", sum(lst))
        elif choice == 5:
            print("length of list is ", len(lst))
        elif choice == 6:
            temp = max(lst)
            lst.remove(temp)
            print(max(lst))
        go = int(input("If you want continue choice enter 1 or 0 :"))
print("Thank you :)")




'''
1.Create a empty list.
2.Get a number how many numbers you want?
3.open for loop
4.Get a numbers 
5.add numbers into list using append function
6.print the largest number using max max() function 
and 
print same as min number min() function.
'''