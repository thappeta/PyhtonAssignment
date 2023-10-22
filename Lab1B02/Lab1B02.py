#Name:Pravalika Rao Chitneni
#CompletionDate:21/10/2023 11.00AM






# to use inbuilt Decimal functions and methods,we have to import their respective packages
from decimal import Decimal

#Below methods will takes String as input paramater and it will be passed to the Decimal methods,result will be calculated


def milesPerGallanon(milesDriven,gallonComsumed):
    mpg=Decimal(milesDriven)/Decimal(gallonComsumed)
    print("Miles driven is "+milesDriven)
    print("Gallons used is "+gallonComsumed)
    print("The MPG is ${:.2f}".format( mpg ))


 #this is main method and it will takes inputs for MilesDriven,GallonsComsumed
if __name__ == '__main__':
    milesDriven=input("Enter total miles driven,up to two decimals : ")
    gallonsComsumed=input("Enter total gallons used,up to two decimals : ")
    milesPerGallanon(milesDriven,gallonsComsumed)
