n=int(input("Enter the total no. of elements"))
elem=[]
for i in range(n):
    num=int(input("Enter the numbers:"))
    elem.append(num)
elem_t= tuple(elem)
total=0
for num in elem_t:
    total+=num
    avg=total/n
print("The total is:",total)
print("The Average is :",avg)
sorted_nums = list(elem_t)
for i in range(len(sorted_nums)):
    for j in range (i+1, len(sorted_nums)):
        if(sorted_nums[i]> sorted_nums[j]):
            sorted_nums[i], sorted_num[j]= sorted_nums[j], sorted_nums[i]
if n%2==1:
    median= sorted_nums[n//2]
else:
    mid1= sorted_nums[n//2-1]
    mid2=sorted_nums[n/2]