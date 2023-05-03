''' faça um programa que leia um nome de usuário e sua senha e não aceite a senha igual ao do nome de usuário, mostrando uma mensagem de erro e voltando 
a pedir as informações '''

name = input("enter your first name: ");

password = input("\n"+"enter your password: ");

while name == password:
  
  print("\n"+"FAIL");
  print("\n"+"say your name and password again")
  
  name = input("\n"+"enter your first name: ");
  
  password = input("\n"+"enter yout password: ");
