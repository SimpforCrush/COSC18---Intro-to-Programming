j = float(input('Enter John Age: '))
s = float(input('Enter Smith Age: '))
a = float(input('Enter Ajay Age: '))

#///if elif////
# if j > s and j > a :
#     print('John is Eldest')
# elif s > a and s > a :
#     print('Smith is Eldest')
# elif a > j and a > s :
#     print('Ajay is Eldest')
# else:
#     print('They are of same age.')

#///////nested if and else///////
# if j > s and j > a :
#     print('John is Eldest')
# else:
#     if s > a :
#         print('Smith is Eldest')
#     else:
#         print('Ajay is Eldest')

#////Match Version/////
match j:
    case _ if j > s and j > a :
        print('John is Eldest')
    case _ if s > a :
        print('Smith is Eldest')
    case _ if j == s and j == a and a == s :
        print('They are of same age.')
    case _ :
        print('Ajay is Eldest')
