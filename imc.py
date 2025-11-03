import datetime

print("Bem-vindo ao Programa de IMC!")
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura (em metros): "))
peso = float(input("Digite seu peso (em kg): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

# Exibir o resultado
print(f"{nome}, seu IMC é {imc:.2f}")
print(f"Classificação: {classificacao}")

data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
with open("historico.txt", "a") as f:
    f.write(f"{data_atual} | {altura} | {peso} | {imc:.2f} | {classificacao}\n")

print("\nHistórico de registros:")
with open("historico.txt", "r") as f:
    print(f.read())
