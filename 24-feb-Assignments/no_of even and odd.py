n = int(input('Enter limit for list: '))
l = []
e = []
o = []
print('Enter', n, 'numbers: ')
for i in range(1, n+1):
    x = int(input())
    l.append(x)
    if(x % 2 == 0):
        e.append(x)
    else:
        o.append(x)
print('The Given List Is ', l)
print('The Odd Numbers List Is ', o)
print('The Even Numbers List Is ', e)