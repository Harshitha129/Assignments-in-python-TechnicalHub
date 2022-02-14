n=int(input("Enter number:"))
digits=0
while(n>0):
    digits=digits+1
    n=n//10
print("The number of digits in the number are:",digits)