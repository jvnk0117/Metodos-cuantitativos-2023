#Loading resources
from random import randint as r
from prettytable import PrettyTable

n = int(input("Enter the number of clients: \n"))
#Client numbers with arrivals 
client = []
timeBetweenArrivals = []
arrivalsTime = []


for i in range(1,n+1):
    client.append(i)

print(client)









# runs_table = PrettyTable()
# runs_table.add_column("Statistics",["Miu","Sigma","Zscore",""])
# runs_table.add_column("Statistics",["Miu","Sigma","Zscore","rerw"])

# print(runs_table)