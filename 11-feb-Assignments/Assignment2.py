sno=(input('Enter sno: '))
sname=(input('Enter name: '))
sgroup=(input('Enter group: '))
s1=int(input('s1 marks: '))
s2=int(input('s2 marks: '))
s3=int(input('s3 marks: '))
s4=int(input('s4 marks: '))
s5=int(input('s5 marks: '))
s6=int(input('s6 marks: '))
total=s1+s2+s3+s4+s5+s6
avg=total/6
if avg>=91:
      print('O Grade')
elif avg>=81:
      print('A Grade')
elif avg>=71:
      print('B Garde')
elif avg>=61:
      print('C Garde')
elif avg>=51:
      print('D Garde')
elif avg>=35:
       print('Pass')
else:
    print('Fail')