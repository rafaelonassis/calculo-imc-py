nome = input("Ola, vamos calcular seu IMC, Qual seu nome? > ")
altura = float(input("Qual sua altura em metros? > "))
peso = float(input("Qual seu peso em Kg? > "))
 
imc = peso / altura**2
  
if imc < 18.5: print("Magreza")
elif imc < 24.9: print("Normal")
elif imc < 30: print("Sobrepeso")
else: print("Obesidade")

print("Seu IMC é: %.2f" % imc)
print("Obrigado por utilizar a calculadora", nome)