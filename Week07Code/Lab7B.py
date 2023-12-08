#Name:Pravalika Rao Chitneni
#CompletionDate:08/12/2023 06.00PM




#here we have imported two packages they are random,random is used to get the RandomNumbers and statistics, from statistics we have imported mean to calculate
#average of the list
import random
from statistics import mean


#methodName:-writingDataToFile
#params:-n-is endLimit to generate the random number
#n1,n2:- they are used to generate the random number between those limits
#fileName:-fileName is used to store the data,which is generated

def writingDataToFile(n, n1, n2,filename):

     nRandomNumbers = [random.randint(n1, n2) for _ in range(n)]
     with open(filename, 'w') as file:
        for num in nRandomNumbers:
            file.write(str(num) + '\n')

#methodName:-read_file_and_process
#savedFileName:-savedFileName is used here because,here we trying to read the data from the file
def read_file_and_process(savedFileName):
    with open(savedFileName, 'r') as file:
        randomNumberList = [int(line.strip()) for line in file]
    return randomNumberList


#methodName:-get_user_input
#params:-userInput
#userInput:-it is for get proper usrInputs from the EndUser and here we have validated that user is entered
#int dataType or not
def get_user_input(userInput):
    while True:
        try:
            user_input = input(userInput)
            return int(user_input)
        except ValueError:
            print("Provide integers as your inputs!")



n = get_user_input("How many random numbers ? ")
n1 = get_user_input("The possible minimun random? ")
n2 = get_user_input("The possible maximum random? ")
fileName=input("File name for saving randon numbers: ")
fileNameToRead=input("The name of file containing the random numbers? ")
while fileNameToRead!=fileName:
    fileNameToRead=input("The name of file containing the random numbers? ")
writingDataToFile(n,n1,n2,fileName)
fileDataList=read_file_and_process(fileNameToRead)
print("The returned list is: ",fileDataList)
resultString="That means :"
resultString=resultString+"The lowest number is " + str(min(fileDataList))+","
resultString=resultString+"The larges number is " + str(max(fileDataList))+","+"\n"
resultString=resultString+"there are " + str(len(fileDataList))+" numbers ,"
resultString=resultString+"The larges number is " +str( round(mean(fileDataList),2))+"."
print(resultString)

