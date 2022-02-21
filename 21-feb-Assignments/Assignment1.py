size = 4
count = 0

for i in range(size):
    for j in range(size):
        print(chr(65 + count), end=" ")
        # changing charater
        count += 1
    print()