def linears(list1, key):
    
    for i in range(len(list1)):
        if list1[i] == key:
            return i  
    return 0  
list1 = [20,10,30,60,50,90,70]
for i in range(len(list1)-1):
    if list1[i+1]<list1[i]:
        list1[i+1],list1[i] = list1[i],list1[i+1]
print("TOO check",list1)
key = int(input("Enter element to search: "))
x = linears(list1, key)

if x != 0:
    print("Yes",key, "Element is present ")
else:
    print("Element not present ")



















