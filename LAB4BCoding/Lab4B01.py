#Name:Pravalika Rao Chitneni
#CompletionDate:11/11/2023 11.00AM


#In this module we performed  many string manipulation
#It seems strings are immutable and so we need to create a new object for the String
#We used here to find the Len:-It's inbuilt function which is used to calculate the lenth of the string and
#And used dictonary to store the Key value pairs to we will get about the vowels are unique and we will get frequency of each vowel
#vowelsWithCaps it's used for to convert the vowels from upper case to lower case
#and here lower() it's inbuilt method in python and it will add the bit value of 32 if it's a upperCase

def stringManipulations(userInput):
    strLen= len(userInput);
    print("The string is {usrInput}".format(usrInput=strLen))
    vowelsWithCaps = ['a','e','i','o','u','A','E','I','O','U']
    vowels = ['a','e','i','o','u']
    usrInput=userInput.casefold()
    count={}.fromkeys(vowels,0)
    vowelsCount=0
    for i in range(strLen):
        if usrInput[i] in vowels:
            count[usrInput[i]]+=1
            vowelsCount+=1
    print("There are a total of",vowelsCount,"vowels")
    for i in count.keys():
        print(i,":",count.get(i))
    print(count)
    resultList=[]
    usrInputList=userInput.split(" ")
    for word in usrInputList:
        resultStr=""
        for i in word:
            if i in vowelsWithCaps:
                resultStr = resultStr+i.lower()
            else:
                resultStr = resultStr+i
        resultList.append(resultStr)
    modifiedString=" ".join(resultList)
    print("The modified string is",modifiedString)



if __name__ == '__main__':
    usrInput=input("Enter a string to process:")
    print("You entered:",usrInput)
    stringManipulations(usrInput)
