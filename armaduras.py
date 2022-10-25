#!/usr/bin/python3

__version__ = '0.1.0'

from msilib.schema import IniFile
import sys
import math

nodo = 6
elementos = 9
reacciones = 3

#formula de nodo
def formula_nodo():
    #2*nodos-elementos-reacciones
    m = 2*nodo-elementos-reacciones
    if m < 0:
        print("Puede ser redundante")
    elif m > 0:
        print("Es inestable")
    elif m == 0:
        print("Es estable")

#coordenadas de cada nodo
coordenadas = [[0,0],[150,0],[300,0],[450,0],[300,75],[150,75]]

A = coordenadas[0]
B = coordenadas[1]
C = coordenadas[2]
D = coordenadas[3]
E = coordenadas[4]
F = coordenadas[5]

#longitud de cada elemento B-A, C-B, E-B, F-B, D-C, E-C, E-D, F-E, F-A

dx = [B[0]-A[0], C[0]-B[0], E[0]-B[0], F[0]-B[0], D[0]-C[0], E[0]-C[0], E[0]-D[0], F[0]-E[0], F[0]-A[0]]
dy = [B[1]-A[1], C[1]-B[1], E[1]-B[1], F[1]-B[1], D[1]-C[1], E[1]-C[1], E[1]-D[1], F[1]-E[1], F[1]-A[1]]

barra_ab = math.sqrt((dx[0])**2+(dy[0])**2)
barra_bc = math.sqrt((dx[1])**2+(dy[1])**2)
barra_be = math.sqrt((dx[2])**2+(dy[2])**2)
barra_bf = math.sqrt((dx[3])**2+(dy[3])**2)
barra_cd = math.sqrt((dx[4])**2+(dy[4])**2)
barra_ce = math.sqrt((dx[5])**2+(dy[5])**2)
barra_de = math.sqrt((dx[6])**2+(dy[6])**2)
barra_ef = math.sqrt((dx[7])**2+(dy[7])**2)
barra_fa = math.sqrt((dx[8])**2+(dy[8])**2)


print('Longitud de cada elemento')
print('AB =',barra_ab)
print('BC =',barra_bc)
print('BE =',barra_be)
print('BF =',barra_bf)
print('CD =',barra_cd)
print('CE =',barra_ce)
print('DE =',barra_de)
print('EF =',barra_ef)
print('FA =',barra_fa)

formula_nodo()


