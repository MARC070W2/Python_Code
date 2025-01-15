"Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,usando a seguinte fórmula: (72.7*altura) - 58"

altura = float(input("informe sua altura: "));

peso_ideal = (72.7*altura) - 58

print("seu peso ideal é: ", peso_ideal);

"Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:"

"Para homens: (72.7*h) - 58"
"Para mulheres: (62.1*h) - 44.7"

altura1 = float(input("informe sua altura homem: "));
altura2 = float(input("informe sua altura mulher: "));

peso_ideal_homem = (72.7*altura1) - 58
peso_ideal_mulher = (62.1*altura2) - 44.7

print("o peso ideal do homem é: ", peso_ideal_homem);
print("o peso ideal da mulher é: ", peso_ideal_mulher);
