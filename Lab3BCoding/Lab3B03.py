#Name:Pravalika Rao Chitneni
#CompletionDate:04/11/2023 11.00AM

#Here we appened the  inputs to append
# used hashmap to store sales values and weekdays
#used max,min,sum,len functions to get what we need






if __name__ == '__main__':
    a=[]

    a.append(float(input("Enter sales in dollars for Mon : ")))
    a.append(float(input("Enter sales in dollars for Tue : ")))
    a.append(float(input("Enter sales in dollars for Wed : ")))
    a.append(float(input("Enter sales in dollars for Thu : ")))
    a.append(float(input("Enter sales in dollars for Fri : ")))
    a.append(float(input("Enter sales in dollars for Sat : ")))
    a.append(float(input("Enter sales in dollars for Sun : ")))

    dict={}
    dict[a[0]]="Mon"
    dict[a[1]]="Tue"
    dict[a[2]]="Wed"
    dict[a[3]]="Thu"
    dict[a[4]]="Fri"
    dict[a[5]]="Sat"
    dict[a[6]]="Sun"

    print("Total sales were ${0:.2f}".format(sum(a)))
    print("Average sales were ${0:.2f}".format(sum(a)/len(a)))
    print("Greatest sales were ${0:.2f}".format(max(a)),dict[max(a)],".")
    print("Least sales were ${0:.2f}".format(min(a)),dict[min(a)],".")



