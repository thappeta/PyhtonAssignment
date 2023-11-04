#Name:Pravalika Rao Chitneni
#CompletionDate:04/11/2023 11.00AM

#Here we used inbuilt method to convert the list to tuple
# used a ::-1 to reverse the whole array in reverse order ::-1 says end to start and interval is 1
if __name__ == '__main__':
    a=[]
    for i in range(5):
        x=i+1
        a.append(input("Enter a number - counter at {usrInput} :".format(usrInput=i+1)))
    print("Now convert the list to a tuple")
    print("Print the tuple in reversed order")
    res=tuple(i for i in a[::-1])
    for i in range(len(res)):
        print("Reverse print - counter at {usrInput} :".format(usrInput=5-i),res[i])

