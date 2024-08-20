# primeiro, reconhecemos as variaveis e adicionamos:
nome = input("Digite seu nome: ")
email = input("Insira seu email: ")
telefone = input("Insira seu numero de telefone: ")

gasolina = int(input('Insira a gasolina gasta em km/l: '))
alcool = int(input('Insira o alcool gasto em km/l: '))
totalkm = 1280 
div = 1280 /gasolina
div2 = 1280 / alcool
print(f"A gasolina gasta é: {div:.2f}km/l")
print(f"A gasolina gasta é: {div2:.2f}km/l")

vlrgaso = float(input('Insira o valor da gasolina: '))
vlralcool = float(input('Insira o valor do alcool: '))
gastogaso = div * vlrgaso
gastoalco = div * vlralcool
print(f"O valor da gasolina gasto mensalmente é: {gastogaso:.2f}")
print("----------------------------------------------")
print(f"O valor gasto do alcool mensalmente é: {gastoalco:.2f}")
print("----------------------------------------------")
media = div / 30
media2 = div2 / 30

print(f"A media de km rodado mensalmente é: {media:.3f}")
print("--------------------------------------------")
print(f"A media gasta mensalmente de alcool é: {media2:.3f}")
print("--------------------------------------------")


