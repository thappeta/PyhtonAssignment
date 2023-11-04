#Name:Pravalika Rao Chitneni
#CompletionDate:04/11/2023 11.00AM

#Used simple if,else,elif conditons for this solution,we can use range function also for this solution
#Range function uses binary Search internally it will takes O(N log(N))
#Here just compared the user Inputs



if __name__ == '__main__':
    while(True):
        userInput=input("Enter number of between 1.00 and 999.99 inclusive:")
        userInput=float(userInput)
        if( userInput>=float(1) and  userInput<=float(999.99) and userInput!=float(555.55)):
            print("Yes,","{0:.2f}".format(userInput),"is valid")
        elif(userInput==555.55):
            print("{0:.2f}".format(userInput),"to exit")
            break
        else:
         print("no,","not valid")

