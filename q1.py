#Using built in fuctions.
n=int(input("Enter a number:"))
num=[]
for i in range(n):
    number=int(input('Enter the numbers:'))
    num.append(number)
max_num=max(num)
min_num=min(num)
print(f"The maximum number is {max_num} and the minimum number is {min_num}")
num.sort()
sorted_num=num
print(f"The sorted numbers is{sorted_num}")
nums=set(num)
print(f"The unique numbers are {nums}")

#Without using built in fuctions.
max=num[0]
min=num[0]
for i in num:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"The maximum number is {max} and the minimum number is {min}")

sorted=[]
for i in range(1,len(num)):
    for j in range(len(num)-i):
        if num[j]>num[j+1]:
            temp=num[j]
            num[j]=num[j+1]
            num[j+1]=temp
sorted.append(num[j])
print(f"The sorted numbers are{num}")

un_num=[]
for i in num:
    if i not in un_num:
        un_num.append(number)
print("The listed unique numbers are:",un_num)