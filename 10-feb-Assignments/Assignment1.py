# Write a program to generate student results whether pass or fail
sno=int (input('Enter student no: '))
sname=input('Enter student name: ')
sgroup=input('Enter student group: ')
s1=int (input('os marks:')) 
s2=int (input('java  marks:')) 
s3=int (input('accounts marks:'))
if s1>=35 and s2>=35 and s3>=35:
    print ('Pass') 
else:
    print('Fail')