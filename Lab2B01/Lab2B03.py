#Name:Pravalika Rao Chitneni
#CompletionDate:28/10/2023 11.00AM

#In this problem we used python in built function Range
#It will checks usrInput is present between two number or not
#and then checked usrInput is even or not
#print output as per the given condition




def rouleteeWheel(userInput):
    if(int(userInput)==0):
        print(userInput,"is green")
    if(int(userInput) in range(1,11)):
        if(int(userInput)%2==0):
            print(userInput,"is red")
        else:
            print(userInput,"black")
    elif(int(userInput)in range(11,19)):
        if(int(userInput)%2==0):
            print(userInput,"is red")
        else:
            print(userInput,"black")
    elif(int(userInput)in range(19,29)):
        if(int(userInput)%2==0):
            print(userInput,"is black")
        else:
            print(userInput,"red")
    elif(int(userInput)in range(29,37)):
        if(int(userInput)%2==0):
            print(userInput,"is red")
        else:
            print(userInput,"black")





if __name__ == '__main__':
    usrInput=int(input("Enter roulette position, o thru 36 -99 to exit:"))
    if(usrInput==99):
        print("Thanks for playing")
    elif(usrInput>36):
        print(usrInput,"is Invalid")
    rouleteeWheel(usrInput)
