n = 12
flag = False
for i in range(2,n):
    if n % i == 0:
        flag = True
        break
if flag == True :
    print("NOT PRIME NUMBER")
else:
    print("PRIME NUMBER")

