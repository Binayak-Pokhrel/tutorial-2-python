#1 answer
'''
a = int(input('Enter 1st number\n'))
b = int(input('Enter 2nd number\n'))

if a>b :
    print(a,'is greater than',b)
elif b>a :
    print(b,'is greater than',a)
'''


#2 answer
'''
a = int (input('Enter the number\n'))

if a%2 == 0 :
    print(a,'is even number.')
elif a%2 != 0:
    print(a,'is odd no.')
else:
    print('none')
'''

#3 answer
'''
a = input('Enter the current day name')

if(a=='tuesday'or a == 'monday' or a=='wednesday' or a =='thursday' or a=='friday'):
    print('Today is',a,'\n Happy weekday!')
elif (a=='saturday'or a=='sunday'):
    print('Today is',a,'\n Enjoy your weekend!')
else:
    print('System error')
'''

#4 answer
'''
name = input('Enter student name\n')
a =int(input('Science Score\n'))
b = int(input('Math Score\n'))
c = int(input('Nepali Score\n'))
d = int(input('Computer Score\n'))
e = int(input('English Score\n'))

print('Student Name =',name)
avg = (a+b+c+d+e)/5
print('average mark =',avg)

if (avg >69 and avg<=100):
    print('A grade')
elif (avg>59 and avg<=69):
    print('B grade')
elif (avg>49 and avg<=59):
    print('C grade')
elif (avg>42 and avg<=49):
    print('D grade')
elif (avg>39 and avg<= 42):
    print('E grade')
elif (avg>=0 and avg<=39):
    print('F grade')
else:
    print('Error. Number you enter is greater than 100')
'''

#5 answer
num = int(input('Enter the no.'))

while (num % i == 0):
            print(num,'is not prime no.')
     