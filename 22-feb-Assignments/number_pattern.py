n = int(input("Enter the number: "));
for i in range(n):
    for j in range(i + 1):
        print(j+1, end="")
    print()
for i in range(n):
    for j in range(n - i - 1):
        print(j+1, end="")
    print()