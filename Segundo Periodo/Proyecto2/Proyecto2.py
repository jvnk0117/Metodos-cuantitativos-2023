#Loading resources
import random as r
from prettytable import PrettyTable
import datetime as d

#Defining number of 
n = int(input("Enter the number of clients: "))

#Data to be displayed in tables
client = []
timeBetweenArrivals = []
arrivalsTime = []
transactionTime = []
serviceStart = []
serviceFinished = []

#raw numerical data (minutes)
arrivalsTimeDirector = []
serviceStartDirector = []
serviceFinishedDirector = []
idleUser = []
idleATM = []



timeBetweenArrivals.append(0)

#Adding clients to the list
for i in range(1,n+1):
    client.append(i)

#Adding the random time between arrivals
for i in range(1,n):
    timeBetweenArrivals.append(r.randint(1,10))

#Adding and setting a fixed time based on minutes
fixedHour = r.randint(0,1380)
arrivalsTimeDirector.append(fixedHour)
arrivalsTime.append(str(d.timedelta(minutes = fixedHour)))


#Setting computed time to a list
for i in range(1,n):
    fixedHour += timeBetweenArrivals[i]
    arrivalsTimeDirector.append(fixedHour)
    arrivalsTime.append(str(d.timedelta(minutes = fixedHour)))


#Generating transaction time
for i in range(0,n):
    transactionTime.append(r.randint(1,5))


#Generating start time and its duration
serviceStartDirector.append(arrivalsTimeDirector[0])
serviceStart.append(str(d.timedelta(minutes=serviceStartDirector[0])))

serviceFinishedDirector.append(serviceStartDirector[0] + (transactionTime[0]))
serviceFinished.append(str(d.timedelta(minutes=serviceFinishedDirector[0])))    

for i in range(0,n-1):
    if serviceFinishedDirector[i] > arrivalsTimeDirector[i+1]:
        serviceStartDirector.append(serviceFinishedDirector[i])
        serviceFinishedDirector.append(serviceStartDirector[i+1] + transactionTime[i+1])
        

    if serviceFinishedDirector[i] < arrivalsTimeDirector[i+1]:
        serviceStartDirector.append(arrivalsTimeDirector[i+1])
        serviceFinishedDirector.append(serviceStartDirector[i+1] + transactionTime[i+1])


for i in range(1,n):
    serviceStart.append(str(d.timedelta(minutes=serviceStartDirector[i])))
    serviceFinished.append(str(d.timedelta(minutes=serviceFinishedDirector[i])))

#computing IDLE TIME

for i in range(0,n):
    idleUser.append(serviceStartDirector[i] - arrivalsTimeDirector[i])

idleATM.append(0)
for i in range(0,n-1):
    idleATM.append(serviceStartDirector[i+1] - serviceFinishedDirector[i])


#Final statistics
totalTransactiontime = 0
totalIdleClient = 0
totalIdleATM = 0

for i in range(0,n):
    totalTransactiontime += transactionTime[i]
    totalIdleClient += idleUser[i]
    totalIdleATM += idleATM[i]

waitCounter = 0
for i in idleUser:
    if i != 0:
        waitCounter+=1

waitATM = totalIdleATM / (arrivalsTimeDirector[-1] - arrivalsTimeDirector[0])



#DIsplay table
runs_table = PrettyTable()
runs_table.add_column('Cliente', client)
runs_table.add_column('Tiempo entre llegadas', timeBetweenArrivals)
runs_table.add_column('Hora de llegada', arrivalsTime)
runs_table.add_column('Tiempo del tramite', transactionTime)
runs_table.add_column('Inicia servicio', serviceStart)
runs_table.add_column('Termina servicio', serviceFinished)
runs_table.add_column('Tiempo cliente espera', idleUser)
runs_table.add_column('Tiempo inactividad ATM', idleATM)

summations = PrettyTable()
summations.add_column("Tiempo total del tramite", [totalTransactiontime])
summations.add_column("Tiempo total de espera del cliente", [totalIdleClient])
summations.add_column("Tiempo total de espera del ATM", [totalIdleATM])

statistics = PrettyTable()
statistics.add_column("Tiempo promedio de espera por cliente",[totalTransactiontime/n ,'min de espera para ser atendidos'])
statistics.add_column("Probabilidad de que un cliente espere en la fila",[waitCounter/n , '%']) 
statistics.add_column("Porcentaje de tiempo que el ATM estuvo inactivo",[waitATM , '%']) 
statistics.add_column("Tiempo promedio de servicio",[totalTransactiontime/n , 'min de realizar el tramite']) 

with open('text3.txt', 'x') as f:
    f.write(str(runs_table))
    f.write(str(summations))
    f.write(str(statistics))


print(runs_table)
print(summations)
print(statistics)

