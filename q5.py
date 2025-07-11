n=int(input("Enter the number required in list:"))
lst=[]
for i in range(n):
    num=int(input("Enter the numbers:"))
    lst.append(num)
    if (i%2==0):
        print(f"{num}")