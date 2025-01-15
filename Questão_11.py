"Faça um Programa que peça 2 números inteiros e um número real.

"Calcule e mostre:"

"o produto do dobro do primeiro com metade do segundo ."
"a soma do triplo do primeiro com o terceiro."
"o terceiro elevado ao cubo."

num1 = int(input("informe um valor inteiro: "));
num2 = int(input("informe um outro valor inteiro : "));
num3 = float(input("informe um valor real: "));

produto_do_dobro = (num1*2)*(num2/2);
soma = (num1*3) + (num3);
produto = num3**3;

print("o resulto da primeira sentença é: ", produto_do_dobro);
print("o resulto da primeira sentença é: ", soma);
print("o resulto da primeira sentença é: ", produto);
