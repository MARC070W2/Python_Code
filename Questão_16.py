Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. 
Informe ao usuário a quantidade de latas de tinta a serem compradas e o preço total.

import math

litros_por_metro = 1 / 3
capacidade_lata = 18
preco_lata = 80.00  

area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

litros_necessarios = area * litros_por_metro

latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)

custo_total = latas_necessarias * preco_lata

print("Área a ser pintada: ", area)
print("Quantidade de latas necessárias: ", latas_necessarias)
print(f"Preço total: R$ ", custo_total)
