#Name:Pravalika Rao Chitneni
#CompletionDate:18/11/2023 10.40AM


#In this python module/script we are checking the given string is palindrome or not
#by using pythonic way,we have reversed the usrInput and stored into another another variable because strings are imutable
#now we have compared the reversedString and usrInputs
#if both strings are same returns true or false


usrInput=input("Enter a string to see if it is a palindrome: ")
reversedInput=usrInput[::-1]
if(usrInput==reversedInput):
    print(usrInput,"is one")
else:
   print(usrInput,"is not one")
