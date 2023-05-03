''' faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto '''

year = int(input("what year do i want to analyze: "));

if year % 4 == 0:
   
   print("this year is leap year", year)

  else: 
    
    print("this year is not leap year", year)
