import math as m
import matplotlib.pyplot as plt



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
W1 = W1 + 0.0001
W1 = int(W1*10000)/ 10000


W2 = float(max(truncatedNumbers2) - min(truncatedNumbers2)) / C2
W2 = W2 + 0.01
W2 = int(W2*100)/ 100



W3 = float(max(truncatedNumbers3) - min(truncatedNumbers3)) / C3
W3 = W3 + 0.001
W3 = int(W3*1000) / 1000


#Calculating intervals 
interval1 = []
interval2 = []
interval3 = []


holder1 = truncatedNumbers1[0]
for i in range(int(C1)):
    interval1.append(holder1)
    holder1 += W1
    holder1 = int(holder1 * 10000) /10000
    interval1.append(holder1)
interval1_tuple = [x for x in zip(*[iter(interval1)]*2)]

holder2 = truncatedNumbers2[0]
for i in range(int(C2)):
    interval2.append(holder2)
    holder2 += W2
    holder2 = int(holder2 * 100) /100
    interval2.append(holder2)
interval2_tuple = [x for x in zip(*[iter(interval2)]*2)]

holder3 = truncatedNumbers3[0]
for i in range(int(C3)):
    interval3.append(holder3)
    holder3 += W3
    holder3 = int(holder3 * 1000) /1000
    interval3.append(holder3)
interval3_tuple = [x for x in zip(*[iter(interval3)]*2)]

#Counting frecuencies in truncated list



total_frecuencies1 = []
counter1 = 0
for i in interval1_tuple:
    for j in truncatedNumbers1:
        if j >= i[0] and j <= i[1]:
            counter1 += 1
    total_frecuencies1.append(counter1)
    counter1=0


total_frecuencies2 = []
counter2 = 0
for i in interval2_tuple:
    for j in truncatedNumbers2:
        if j >= i[0] and j <= i[1]:
            counter2 += 1
    total_frecuencies2.append(counter2)
    counter2 = 0


total_frecuencies3 = []
counter3 = 0
for i in interval3_tuple:
    for j in truncatedNumbers3:
        if j >= i[0] and j <= i[1]:
            counter3 += 1
    total_frecuencies3.append(counter3)
    counter3 = 0



plt.plot(interval1_tuple, total_frecuencies1, label = "set 1")
plt.show()
