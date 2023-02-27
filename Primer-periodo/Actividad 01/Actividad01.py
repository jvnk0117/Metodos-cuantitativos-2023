
#reading data from sources
with open('Primer-periodo\Actividad 01\data01.txt','r') as f:
    data1 = [line.strip() for line in f] 
with open('Primer-periodo\Actividad 01\data02.txt','r') as f:
    data2 = [line.strip() for line in f] 
with open('Primer-periodo\Actividad 01\data03.txt','r') as f:
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


#truncating decimals from datasets 

truncateNumbers1 = []
truncateNumbers2 = []
truncateNumbers3 = []

for number in dataNumbers1:
    value1 = '%.4f'%(number)
    truncateNumbers1.append(value1)

for number in dataNumbers2:
    value2 = '%.2f'%(number)
    truncateNumbers2.append(value2)

for number in dataNumbers3:
    value3 = '%.3f'%(number)
    truncateNumbers3.append(value3)

