from decimal import Decimal

# input options

name = input('Enter Your Name : ')
print('Your name : ',name)
print (type(name))

age = int(input('Enter Your Age : '))
print('Your age : ',age)
print (type(age))

value = float(input('Enter Your Rate - two decimals : '))
print('Your value : ',value)
print (type(value))


num = input('Enter any number : ')
print ('The variable num is ' + num)
print (type(num))


dec = Decimal(input("please enter the decimal value "))
print ('The variable dec is ' , dec)
print (type(dec))

a,b=input("a"),input("b")
print("intialized a",a,"intialized b",b,"at once")

