#Write a program to remove zero elements from the list and find the total count of non zero elements and display them
a = []
temp = []
Number =int(input("enter the total no.of list elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    a.append(value)
for j in range(len(a)):
    if a[j] != 0:
        temp.append(a[j])
    else:
        zeros.append(a[j])
count = len(temp)
print("number of non zero elements: ",count)
print(temp)