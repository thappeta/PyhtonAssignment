#Name:Pravalika Rao Chitneni
#CompletionDate:28/10/2023 11.00AM


#magicDateCheck will take int DataType variables,because here we need do some multiplication operation
#In magicDateCheck function we did day and month multiplication and compared to year
#if its true we print "Its a magic date
#else it not a magic date






def magicDateCheck(mm,dd,yy):
    if(mm*dd==yy):
        print(mm,dd,yy,"IS a magic date")
    else:
        print("The entered date is invalid")


if __name__ == '__main__':
    mm=int(input("Enter mm for month:"))
    dd=int(input("Enter dd for day:"))
    yy=int(input("Enter yy for year:"))
    magicDateCheck(mm,dd,yy)

