n = int(input('Enter n : '))
se = 0
so = 0
for i in range(1, n+1):
    if(i % 2 == 0):
        se = se+i
    else:
        so = so+i
print('Sum of even numbers = ', se)
print('Sum of odd numbers = ', so)