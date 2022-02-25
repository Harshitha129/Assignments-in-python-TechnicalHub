def prime(x):
    s = 0
    for i in range(1, x+1):
        if(x % i == 0):
            s += 1
    if(s == 2):
        return True
    return False


n = int(input('Enter limit for list: '))
l = []
c = 0
print('Enter', n, 'numbers: ')
for i in range(1, n+1):
    x = int(input())
    l.append(x)
    if(prime(x)):
        c += 1
print('The number of prime numbers in given list is', c)