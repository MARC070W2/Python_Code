Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.

num1 = float(input("informe seu ganho por hora: "));
num2 = int(input("informe a qtd de horas trabalhadas no mes: "));

salario_bruto = num1*num2;
IR = salario_bruto*0.11;
INSS = salario_bruto*0.08;
sindicato = salario_bruto*0.05;

salario_liquido = salario_bruto - (IR + INSS + sindicato);

print("o salario liqido é : ", salario_liquido);
print("o salario bruto é de : ", salario_bruto);
print("o valor descontado do IR é de : ", IR);
print("o valor descontado do INSS é de : ", INSS);
print("o valor descontado do sindicato é de : ", sindicato);
