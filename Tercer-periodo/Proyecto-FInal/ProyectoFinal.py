import numpy as np
from random import randint, choice
nameFile = open("Tercer-periodo/Proyecto-FInal/names.txt",'r')
nameData = nameFile.read()
nameList = nameData.split('\n')

winner = False

n = int(input('Enter the number of platoons: '))

platoonLedger = {}
for i in range(1,n+1):
    platoonLedger[i] = randint(30,50)



def matrixGeneration(n):
    header = np.random.rand(n, n)
    np.fill_diagonal(header, 0)
    header /= header.sum(axis=1, keepdims=True)
    soldierMatrix = np.round(header,2)
    return soldierMatrix



def calibrateMatrix(matrix):
    actualSize = matrix.shape[0]
    calibratedMatrix = np.zeros((actualSize - 1, actualSize - 1))
    calibratedMatrix[:actualSize-1, :actualSize-1] = matrix[:-1, :-1]
    np.fill_diagonal(calibratedMatrix, 0)
    calibratedMatrix /= calibratedMatrix.sum(axis=1, keepdims=True)
    formatedCalibratedMatrix = np.round(calibratedMatrix,2)
    return formatedCalibratedMatrix
    
mainMatrix = matrixGeneration(n)


def platoonConflict(ledger):
    platoonAttacking = randint(0,n)
    attackValue = randint(0,10) / 100

    for row in mainMatrix[platoonAttacking]:
        if row.index(platoonAttacking) == platoonAttacking:
            continue
        print(row)
    

        
        

def platoonConflict(matrix, winner):

    for rows in matrix:
        print(rows)

    print('====================================')

    for k,v in platoonLedger.items():
        print(f'Group {k} : {v}')

    # while 0 not in platoonLedger.values():
    #     platoonAssasulting = randint(1,n)
    #     attackValue = randint(0,10) / 100

    #     if platoonAssasulting == platoonLedger.keys():
            
    #         print(f'\nGroup {soldierAssasulting} is atttacking')


    print('Recalibrating stochastic matrix: \n ')
    matrix = calibrateMatrix(matrix)
    for index,(rows) in enumerate(matrix, 1):
        print(f'{index}  {rows}')

    print('====================================')

    
    if len(platoonLedger) == 1:
        winner = True
        for k in platoonLedger.keys():
            print(f'Grupo {k} es el vencedor!')

    return winner

platoonConflict(mainMatrix,False)


platoonAttacking = randint(0,n-1)
for row in mainMatrix[platoonAttacking]:
    # if row.index(platoonAttacking) == platoonAttacking:
    #     continue
    print(row)



# for index,(k,v) in enumerate(soldierLedger.items(),1):
#     print(f'{index} - {k} : {v} assault units.')


