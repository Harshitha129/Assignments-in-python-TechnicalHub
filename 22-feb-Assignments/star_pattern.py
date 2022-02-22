n = int(input("Enter the number: "))
i = n - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= n - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

i = 0
while i <= n - 1:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= n - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1
