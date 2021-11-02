from sympy import *
from math import pi
import numpy as np
import pandas as pd

"""Criação das listas e constantes utilizadas no problema."""
N = [1, 2, 3, 4]; L = 2; F_list = []
h = 663 * pow(10, -36); m = 3.1*pow(10, -31)
List_x = list(map(lambda a: a/100000, range(0, 2*pow(10, 5), 1000)))
List_l = list(map(lambda a: a/10000, range(10, 100)))
List_Energy = []

"""Criação da Função de Onda do sistema unidimensional."""
def F(n, x):
    return sqrt(2/L)*sin(((n*round(pi, 2)*x)/L))
n, x, z = symbols("n x z")

"""Loop para o cálculo dos valores da função de onda, de sua districuição de densidade
e de sua distribuição acumulativa."""
for i in N:
    for j in List_x:
        WAVE = F(n, x).subs([(n, i), (x, j)])
        DENSITY = WAVE**2
        PROBABILITY = integrate((F(n, x).subs(n, i))**2, (x, j))
        F_list.append([i, j, round(WAVE, 2), round(DENSITY, 2), round(PROBABILITY, 2)])
        print(i, j, WAVE, DENSITY, PROBABILITY)

"""Loop para o cálculo da variação de energia entre estados vizinhos n=3 e n=4
em função da variação do comprimento da caixa, de 0.001 à 0.02 m."""
for i in List_l:
    ENERGY = ((h**2)*7)/(8*m*i**2)
    List_Energy.append([i, ENERGY])
    print(i, ENERGY)

Energy_array = np.array(List_Energy)
F_array = np.array(F_list)

Results_A = pd.DataFrame({"Level": F_array[0::, 0], "Length": F_array[0::, 1],
                          "Wave": F_array[0::, 2], "Density": F_array[0::, 3],
                          "Probability": F_array[0::, 4]})
Results_B = pd.DataFrame({"Level": Energy_array[:, 0], "Energy": Energy_array[:, 1]})

with pd.ExcelWriter(r'C:\Users\Romulo\Desktop\Quantica\EDs\ED3\Resultados_A.xlsx') as archive:
    Results_A.to_excel(archive, sheet_name="Python results", index=False)
with pd.ExcelWriter(r'C:\Users\Romulo\Desktop\Quantica\EDs\ED3\Resultados_B.xlsx') as archive:
    Results_B.to_excel(archive, sheet_name="Python results", index=False)