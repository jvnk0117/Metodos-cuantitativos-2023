#Loading resources
import random as r
from prettytable import PrettyTable
import datetime as d

#Defining number of 
n = int(input("Enter the number of clients: "))


client = []
timeBetweenArrivals = []
arrivalsTime = []
transactionTime = []

timeBetweenArrivals.append(0)

for i in range(1,n+1):
    client.append(i)
for j in range(1,n):
    timeBetweenArrivals.append(r.randint(1,10))

fixedHour = r.randint(0,1380)
arrivalsTime.append(str(d.timedelta(minutes = fixedHour)))

for k in range(1,n):
    fixedHour += timeBetweenArrivals[k]
    arrivalsTime.append(str(d.timedelta(minutes = fixedHour)))


for j in range(0,n):
    transactionTime.append(r.randint(1,5))
    

runs_table = PrettyTable()
runs_table.add_column('Cliente', client)
runs_table.add_column('Tiempo entre llegadas', timeBetweenArrivals)
runs_table.add_column('Hora de llegada', arrivalsTime)
runs_table.add_column('Tiempo del tramite', transactionTime)


print(runs_table)