#Name:Pravalika Rao Chitneni
#CompletionDate:11/11/2023 11.00AM


#In this module it's all about convertions
#First metersPersMiles are converted and then we started all conversions are per our requirement
#for rounding we used floor inbuilt method to converted by rounding to floor
import math


def convert_distance(meterPerMiles,metersPerFoot,InchesToFoot,userInput):
    miles = userInput / meterPerMiles
    feetDecimals = miles % 1
    feet = feetDecimals * meterPerMiles / metersPerFoot
    inches_decimal = feet % 1
    inches = inches_decimal * InchesToFoot
    return int(math.floor((miles))), int(feet), int(inches)


breakCondition = 1

while breakCondition != 0:
    breakCondition = float(input("Enter meter to convert 0 to exit: "))
    if breakCondition == 0:
        break
    meterPerMiles = 1/0.000621371
    metersPerFoot = 1/(5280*0.000621371)
    InchesToFoot = 12

    miles, feet, inches = convert_distance(meterPerMiles,metersPerFoot,InchesToFoot,breakCondition)
    print(f"{miles} Miles, {feet} Feet, and {inches} Inches.")

