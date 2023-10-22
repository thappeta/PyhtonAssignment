#Name:Pravalika Rao Chitneni
#CompletionDate:21/10/2023 11.00AM


# This function will takes name,city ,sports,Major as inputs and then printed by appending to the existing String
def printStatments(name, city, sports, major):
    print("My name is " + name)
    print("I was born in " + city)
    print("My favorite team is " + sports)
    print("My undergraduate is " + major)


# this is main method and it will takes inputs for Name,City,Sports,Major and those inputs will be
# passed to the printStatment function
if __name__ == '__main__':
    name = input("What's your name:")
    city = input("Where were you born?")
    sports = input("Your favourite team?")
    major = input("What is your undergraduate major?")
    printStatments(name, city, sports, major);
