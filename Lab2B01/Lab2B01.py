#Name:Pravalika Rao Chitneni
#CompletionDate:28/10/2023 11.00AM


#Used HashMap here
#Key are integers values and they are unique and so they are taken as keys.
#Here dict is intialized null and then added key,value pairs
# dict.get --->this method is used for getting values based on the key

#Conditon:If user gave number more than 10 then ,function will give info to user please enter number 0 to 10


def convertInttoRomanNumberical(userInput):

    dict={}
    dict[1]="I"
    dict[2]="II"
    dict[3]="III"
    dict[4]="IV"
    dict[5]="V"
    dict[6]="VI"
    dict[7]="VII"
    dict[8]="VIII"
    dict[9]="IX"
    dict[10]="X"

    print("Roman Numberal",dict.get(userInput))

if __name__ == '__main__':
    userInput=input("Enter a number from one to 10:")
    if(int(userInput)>10):
        print("Number entered from one to 10:",userInput)
    else:
        convertInttoRomanNumberical(int(userInput))
