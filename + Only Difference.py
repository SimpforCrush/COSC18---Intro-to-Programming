##Given two numbers, display the difference of two integers.
## Sample:  10 - 5 = 5
##          5 - 10 = 5  (instead of -5)
## There shouldn't be a negative number.

#////solution 1:////
# n1 = int(input('Enter n1: '))
# n2 = int(input('Enter n2: '))
#
# if n1 > n2:
#     d = n1 - n2
#     print(d)
# else:
#     d = n2 - n1
#     print(d)

#/////solution 2////
# n1 = int(input('Enter n1: '))
# n2 = int(input('Enter n2: '))
#
# if n1 - n2 >= 0:
#     print(n1-n2)
# else:
#     print(n2-n1)

#///Match Version

n1 = int(input('Enter n1: '))
n2 = int(input('Enter n2: '))

match n1:
    case _ if n1 > n2
        print(n1-n2)
    case _:
        print(n2-n1)

