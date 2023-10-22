from decimal import Decimal
import platform

# test the installed version
print('This is python version {}'.format(platform.python_version()))

print('My name is'.format("Pralika"))
print('I am doing my master in '.format("Computer sciences"))
print("The MPG is ${:.2}".format( str(Decimal(10))))
