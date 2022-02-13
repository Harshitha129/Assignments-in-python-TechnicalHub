cname = input('Enter customer name: ')
cpn=int(input('Enter customer phone number: '))
noodle=int(input('Enter no.of noodle packets: '))
soap=int(input('Enter no.of soap boxes: '))
perfume=int(input('Enter no.of perfumes: '))
sting=int(input('Enter no.of sting bottles: '))
shampoo=int(input('Enter no.of shampoo bottles: '))
cc=input('Enter coupon code: ')
nc=149
sc=159
pc=300
stc=40
shc=192
bill=(nc*noodle)+(sc*soap)+(pc*perfume)+(stc*sting)+(shc*shampoo)
if bill<1000:
    print('Invalid coupon code')
else:
    if bill>5000:
        if(cc=='HELLO'):
            dis=bill*10/100
            tax=bill*10/100
    if bill>3000:
        if(cc=='HELLO'):
            dis=bill*8/100
            tax=bill*10/100
    if bill>2000:
        if(cc=='HELLO'):
            dis=bill*5/100
            tax=bill*18/100
    if bill>1000:
        if(cc=='HELLO'):
            dis=bill*3/100
            tax=bill*18/100
    main_bill=bill-(dis+tax)
    print('BILL AMOUNT: ',main_bill)