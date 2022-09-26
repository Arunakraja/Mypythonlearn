lst =[]
num = 5 #int(input('Enter number of number want : '))
for n in range(num):
    numbers = int(input('Enter the number :'))
    lst.append(numbers)
lst.sort()
print("After Sorting",lst)
print("Second largest number is",lst[-2])


