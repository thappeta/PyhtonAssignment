import math

message = "python Is Easy to Use."

#caseflod()
#----------
#This is inbuilt function which provided by the python
#Main functionality of this method
#This method more less a bruteforce one because it won't bother it will convert everything into lowercase
#print(message.casefold())
#endswith()
#it will checks last indices of the targetString is present in the source
#Here it will compares the characters from last
#If any character is not matched returns true or returns false
#It's is case sensitive
#print(message.endswith("Use."))# true
#print(message.endswith("use."))#false
#isalnum()
#Its checks is there any digit is available in the
#just compare each character bitsize and checks bits is falling out of the captial and small cases of the
#print(message.isalnum())
#istitle()
#It checks each word in the sentence are starting with the Captial letter or not
#print(message.istitle())
#Python join() is an inbuilt string function in Python used to join elements of the sequence separated by a string separator.
# This function joins elements of a sequence and makes it a string.
#print("-".join(message))



#It will rounds the value to upper decimal
a=2.35
print("Ceil",math.ceil(a))

#It will find the value the GCD of the two values
a=12
b=24
print("GCD",math.gcd(a,b))

#It find the values of the square root of the given value
a=16
print("Sqrt of the value",math.sqrt(16))

#It will find the product of the given values
#sequence(a,b,c) --> a*b*c
sequence = (3,5,10)
print("multication ",math.prod(sequence))


#It will find the value of the
print ("Sin value of zero ",math.sin(0.00))
print ("Sin value of 90 ",math.sin(math.pi/2))

