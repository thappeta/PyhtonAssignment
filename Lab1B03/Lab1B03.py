#Name:Pravalika Rao Chitneni
#CompletionDate:21/10/2023 11.00AM



# here used float to convert the string data type to float
# used format method to get only 2 decimals for result

def mealCharges(mealCost):
    print("Meal costs $"+mealCost)
    print("Tip is ${:.2f}".format( float(mealCost)*20/100 ))
    print("Tax is ${:.2f}".format( float(mealCost)*5/100) )

 #this is main method and it will takes inputs for MealCost
if __name__ == '__main__':
    mealCost=input("Enter meal amount,dollars and cents: ")
    mealCharges(mealCost);


