#Desenvolvimento da lógica de menu
import time
import os

options = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Exponenciação']
numberofoptions = len(options) -1
turn = 0
string = 'e' # Usaremos para no futuro
choice = 0

def start():
   options = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Exponenciação']
   numberofoptions = len(options) -1
   turn = 0
   while turn <= numberofoptions:
      print(turn, ":", options[turn])
      turn += 1

#Desenvolvimento da mensagem da escolha pelo usuário com loop de voltar
   choice = int(input("\nEscolha a operaçao que deseja realizar:"))
   x = 0
   while x <1: 
      if choice == 0:
         print("\n+ Escolhida")
         x +=1
      elif choice == 1:
         print("\n - Escolhida")
         x +=1
      elif choice == 2:
         print("\n x Escolhida")
         x +=1
      elif choice == 3:
         print("\n/ Escolhida")
         x +=1
      elif choice == 4:
         print("\n Exponenciação Escolhida")
         x +=1
      else: 
         print("\nPor favor Escolha uma opção correspondente")
         choice = int(input("Escolha a operaçao que deseja realizar:"))

   print("\nLoading....")
   time.sleep(1)

#Desenvolvendo as entradas de valores E #Verificando se os valores são números
   y = 0
   string = 'e' # Usaremos para no futuro
   validation = 0 #usaremos em breve, tenha paciência
   while validation <1:
      firtsvalue = int(input("\nQual primeiro valor?"))
      if type(firtsvalue) != type(string):
       validation += 1
      else:
       print("\nO Valor informado não é um número, por favor digite um número")
   while validation <2:    
       secondvalue = int(input("\nQual o segundo valor?"))
       if type(secondvalue) != type(string):
        validation += 1
       else:
        print("\nO Valor informado não é um número, por favor digite um número") 

#Desenvolvendo as operações com a "choice escolhida" e mostrando na tela
   if choice == 0: #soma
    print(firtsvalue, '+', secondvalue , '=', firtsvalue+secondvalue)
   elif choice == 1: #Subtração
    print(firtsvalue, '-', secondvalue , '=', firtsvalue-secondvalue)
   elif choice == 2: #Multiplicação
    print(firtsvalue, 'x', secondvalue , '=', firtsvalue*secondvalue)
   elif choice == 3: #Divisão
    print(firtsvalue, '/', secondvalue , '=', firtsvalue/secondvalue)
   elif choice == 4: # Exponenciacão
    print(firtsvalue, 'ˆ', secondvalue , '=', firtsvalue**secondvalue)
   else:
    print("\nPor favor Digite uma opção dentre as indicadas")

#Desenvolvimento da opção de retorno ou finalização 
   while y<1:
      finaloption = int(input("\nDeseja fazer outra opção? 0 - SIM, 1 - NÃO"))
      if finaloption == 1:
         y +=1
         print("\nMuito Obrigado até a Próxima, programa encerrado")
      elif finaloption == 0:
       os.system('clear')
       start()
      else:
         print("\nDigite 0 - SIM ou 1 - NÃO")
start()




