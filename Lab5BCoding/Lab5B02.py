#Name:Pravalika Rao Chitneni
#CompletionDate:18/11/2023 10.40AM

import random

#is_prime(parameter)
#Accepts usrInput
#Returns boolean true/false
#This method checks passed parameter is primeNumber or Not
def is_prime(generatedNumber):
    if generatedNumber <= 1:
        return False
    for i in range(2, int(generatedNumber**0.5) + 1):
        if generatedNumber % i == 0:
            return False
    return True

#generate_random_number(parameter1,parameter2)
#Accepts two userInputs
#Returns primeNumber which is generated randomly
def generate_random_number(usrInput_2, usrInput_3):
    while True:
        generated_RandomNumber = random.randint(usrInput_2, usrInput_3)
        if is_prime(generated_RandomNumber):
            return generated_RandomNumber

#countCheck(parameter_1,parameter_2)
#it will checks length of the primesnumbers count and checks count

def countCheck(usrInput_2, usrInput_3):
    count = 0
    for num in range(usrInput_2, usrInput_3 + 1):
        if is_prime(num):
            count += 1
    return count

#number_of_primes_in_the_range(userInput1, userInput2, userInput3)
#In this method we need to collect the primeNumbers which are generated randomly
#Here we used set to collect the unique numbers
#And the set was type casted to list
#List was manipulated
#printed list and reversed list and find the max and min of the list
def number_of_primes_in_the_range(userInput1, userInput2, userInput3):
    primes = set()
    while len(primes) < userInput1:
        random_prime = generate_random_number(userInput2, userInput3)
        primes.add(random_prime)
    resultList= list(primes)
    print("The generated random number list:")
    print(resultList)
    print(resultList[::-1])
    print("The minimum and maximum prime numbers are :",max(resultList),"and",min(resultList))


#main()
#Is's more like a wrapper method
#because we have called all the methods
#and achieved the output
def main(input_values):

    while True:
        try:
            if len(input_values) != 3:
                raise ValueError()

            usrInput_1,usrInput_2, usrInput_3=input_values
            if usrInput_1 <= 0:
                raise ValueError()

            if usrInput_2 >= usrInput_3:
                raise ValueError()

            if countCheck(usrInput_2,usrInput_3) < usrInput_1:
                raise ValueError()
            break
        except ValueError as e:
            print()

    number_of_primes_in_the_range(usrInput_1,usrInput_2,usrInput_3)

if __name__ == "__main__":
    print("Provide inputs of 3 integers from the keyboard")
    print("The 1st is the number of unique prime numbers to be created;")
    print("The 2nd and 3rd define the range of those prime numbers.")
    input_values = list(map(int, input("Enter those 3 integers seperated by space :").split()))
    main(input_values)




