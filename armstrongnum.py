num = 153
sum = 0
temp = num
while temp>0:
    digit = temp % 10 #3
    sum += digit **3 # cube
    temp = temp//10 #15
if num == sum:
    print("The given number armstong")
else :
    print("Not a armstrong")
