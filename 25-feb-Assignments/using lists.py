#Write a program to move Positive numbers to first and Negative numbers to last
NumList = []
Positive = []
Negative = []

Number = int(input("Enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])
print(Positive, Negative)