#Loading the required packages
from prettytable import PrettyTable
from math import sqrt
#Reading dataset and converting it into a sorted list
chiFile = 'Proyecto1/chi_data.txt'
runsfile = 'Proyecto1/runs_data.txt'

def fileToList(file):
    with open(file,'r') as f:
        data = [line.strip() for line in f] 
    fileList = []

    for line in data:
        value = float(line)
        fileList.append(value)
    return fileList

#Creating linear congruential method

def linearCongruentialMethod(xi, a, c, m, iter):
    randomNumbers=[]
    if iter <= 0:
        raise ValueError("Incorect number of iterations, must be above than cero")
    else:
        for i in range(1,iter +1):

            x = ((a * xi)+ c) % m 
            r = x/m
            randomNumbers.append(r)
            
            xi = x

    table = PrettyTable()
    table.add_column('LCG random numbers', randomNumbers)
    return table

#GeneratedRandomNumbers = linearCongruentialMethod(6,32,3,80,10)

#print(GeneratedRandomNumbers) #call at the end ofthe program




def chiSquare(list):
    #Computing interval list and formating it

    intervalList = []

    #given a number of clases C= 10 and a weight of 
    holder = 0
    for i in range(0,10): 
        intervalList.append(holder / 10)
        holder += 1
        intervalList.append(holder / 10)

    intervalListTuple = [x for x in zip(*[iter(intervalList)]*2)]

    formatedList = []
    for j in intervalList:
        j = "{0:.4f}".format(j)
        formatedList.append(j)

    formatedListTuple = [x for x in zip(*[iter(formatedList)]*2)]

    #getting observed results
    observedList = []
    counter = 0
    for i in intervalListTuple:
        for j in list:
            if j >= i[0] and j <= i[1]:
                counter += 1


        observedList.append(counter)
        counter = 0

    #Getting expected values, since we have 30 values and 10 clases, 30 / 10 = 3
    expectedList = []
    for i in observedList:
        expectedList.append(3)


    #Computing chi square table
    chisquareList = []
    for i in range(0,10):
        chiSquareVal = (observedList[i] - expectedList[i] ) ** 2 / expectedList[i]
        chisquareList.append(chiSquareVal)

    x_total  = 0
    for j in chisquareList:
        x_total += j 

    formatedChiSquareList = []
    for j in chisquareList:
        j = "{0:.4f}".format(j)
        formatedChiSquareList.append(j)

    chi_table = PrettyTable()
    chi_table.add_column('Intervals',formatedListTuple)
    chi_table.add_column('Observed (O)',observedList)
    chi_table.add_column('Expected (E)', expectedList)
    chi_table.add_column('(O - E) ^ 2 / E', formatedChiSquareList)

    print('H0: Generated numbers are not different from the uniform distribution')
    print('H1: Generated numbers are different from the uniform distribution')
    print('\n')
    if x_total > 16.91:
        print('Since', round(x_total,4),' > 16.91, H0 is rejected')
    else:
        print('Since', round(x_total,4),' < 16.91, H0 is accepted')
    print('---------------------------------------------------- X\u00b2: ',round(x_total,4))

    return(chi_table)
  

def runsTest(list):
    sign_list = []
    for i in range(len(list) - 1 ):
        if list[i+1] > list[i] and i < len(list):
            sign_list.append('+')
        elif list[i+1] < list[i] and i < len(list):
            sign_list.append('-')
    total_signs = len(sign_list)

    runs = 0
    for j in range(len(sign_list) - 1):
        if sign_list[j+1] != sign_list[j]:
            runs += 1
    total_runs = runs + 1
    
#Statistics
    print("H0: Appereance of the numbers is random")
    print("H1: Appereance of the numbers is not random")

    miu = round((2 * total_signs - 1) / 3, 4)
    sigma = round(sqrt((16 * total_signs - 29) / 90), 4)
    zscore = round((runs - miu) / sigma, 4)
    if zscore < 1.96:
        print("Since |" + str(zscore) + "| < |1.96|, H0 is not rejected")
    else:
        print("Since |" + str(zscore) + "| > |1.96|, H0 is rejected")



    runs_table = PrettyTable()
    runs_table.add_column('Statistics', 'Miu', 'Sigma','Zscore')
    runs_table.add_column('Values',miu,sigma,zscore)
    return(runs_table)
runsList = fileToList(runsfile)
print(runsTest(runsList))



