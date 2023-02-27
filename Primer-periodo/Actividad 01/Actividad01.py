import math as m


#reading data from sources
with open('Primer-periodo/Actividad 01/data01.txt','r') as f:
    data1 = [line.strip() for line in f] 
with open('Primer-periodo/Actividad 01/data02.txt','r') as f:
    data2 = [line.strip() for line in f] 
with open('Primer-periodo/Actividad 01/data03.txt','r') as f:
    data3 = [line.strip() for line in f] 

#cleaning data to float numbers
dataNumbers1 = []
dataNumbers2 = []
dataNumbers3 = []

for line in data1:
    value = float(line)
    dataNumbers1.append(value)

for line in data2:
    value = float(line)
    dataNumbers2.append(value)

for line in data3:
    value = float(line)
    dataNumbers3.append(value)


#truncating decimals from datasets and sorting them

truncatedNumbers1 = []
truncatedNumbers2 = []
truncatedNumbers3 = []

for number in dataNumbers1:
    value1 = '%.4f'%(number)
    truncatedNumbers1.append(float(value1))

for number in dataNumbers2:
    value2 = '%.2f'%(number)
    truncatedNumbers2.append(float(value2))

for number in dataNumbers3:
    value3 = '%.3f'%(number)
    truncatedNumbers3.append(float(value3))

truncatedNumbers1.sort()
truncatedNumbers2.sort()
truncatedNumbers3.sort()

#obtaining size of EACH list (N)

N1 = len(truncatedNumbers1)
N2 = len(truncatedNumbers2)
N3 = len(truncatedNumbers3)


#Obtaining number of classes (C)

C1 = float(m.ceil(1 + 3.3*m.log(N1,10)))
C2 = float(m.ceil(1 + 3.3*m.log(N2,10)))
C3 = float(m.ceil(1 + 3.3*m.log(N3,10)))


#Obtaining class width (W)
W1 = float(max(truncatedNumbers1) - min(truncatedNumbers1)) / C1
W1 = '%.4f'%(W1) 

W2 = float(max(truncatedNumbers2) - min(truncatedNumbers2)) / C2
W2 = '%.2f'%(W2 + 0.01) 

W3 = float(max(truncatedNumbers3) - min(truncatedNumbers3)) / C3
W3 = '%.3f'%(W3 + 0.001) 


#Calculating intervals 

