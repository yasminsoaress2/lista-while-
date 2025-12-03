#um programa que peça uma nota (float), entre zero e dez. Mostre uma mensagem caso o valor seja inválido, e continue pedindo até que o usuário informe um valor válido. Imprima a nota válida digitada ao final, dizendo se com a nota o usuário foi aprovado ou não (aprovado >= 7.0)
nota = float(input("Digite uma nota de 0 a 10: "))
while nota < 0 or nota > 10:
    print("Valor inválido! A nota deve estar entre 0 e 10")
    nota = float(input("Digite novamente: "))
print(f"Sua nota válida é {nota}")   
if nota >= 7:
    print("Parabéns! Você foi aprovado!")
else:
    print("Infelizmente você foi reprovado.")


#um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando  a pedir as informações
nome_usuario = input("Digite o nome de usuário: ")
senha = input("Digite uma senha: ")
while senha == nome_usuario:
    print("Erro! A senha não pode ser igual ao nome de usuário.")
    senha = input("Digite uma senha diferente: ")
print("Usuário e senha cadastrados com sucesso!")


#criar um programa que peça, continuamente, para o usuário digitar um número e, logo em seguida, mostrar seu dobro. Quando o valor 0 (zero) for lido, o programa deverá cessar sua execução
numero = float(input("Digite um número (0 para sair): "))
while numero != 0:
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")
    numero = float(input("Digite outro número (0 para sair): "))
    print("Programa encerrado.")


#um programa que peça dois números naturais, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize o operador de potência da linguagem (**). Mostre uma mensagem caso os valores não sejam naturais e continue pedindo até que o usuário informe valores válidos. Valide cada valor separadamente. OBS: números naturais são os números inteiros positivos
base = int(input("Digite um número natural: "))
while base <= 0:
    print("Valor inválido! O número deve ser natural")
    base = int(input("Digite novamente um número natural: "))

expoente = int(input("Digite um expoente natural: "))
while expoente <= 0:
    print("Valor inválido! O expoente deve ser natural")
    expoente = int(input("Digite novamente um expoente natural: "))

resultado = 1
for _ in range:
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")



#programa que peça, continuamente, para o usuário digitar um número e, logo em seguida, mostrar seu dobro. Quando o valor 0 (zero) for lido, o programa deverá cessar sua execução
numero = float(input("Digite um número (0 para sair): "))
while numero != 0:
    dobro = numero * 2
    print(f"O dobro de {numero} é {dobro}")
    numero = float(input("Digite outro número (0 para sair): "))
    print("Programa encerrado.")


#um algoritmo para ler vários números e informar quantos números entre 100 e 200 foram digitados. Quando o valor -1 (um negativo) for lido, o algoritmo deverá cessar sua execução
contador = 0
numero = float(input("Digite um número (-1 para sair): "))
while numero != -1:
    if 100 <= numero <=200:
        contador += 1
    numero = float(input("Digite outro número (-1 para sair): "))
    print(f"Números entre 100 e 200 digitados: {contador}")


#algoritmo para ler a idade de várias pessoas e imprimir: o total de pessoas com menos de 21 anos, e o total de pessoas com mais de 50 anos. Quando o valor -1 (um negativo) for lido, o algoritmo deverá cessar sua execução
idade = int(input("Digite uma idade (ou -1 para sair): "))
menos_21 = 0
mais_50 = 0

while idade != -1:
    if idade < 21:
        menos_21 += 1
    if idade > 50:
        mais_50 += 1

    idade = int(input("Digite uma idade (ou -1 para sair): "))

print(f"Total de pessoas com menos de 21 anos: {menos_21}")
print(f"Total de pessoas com mais de 50 anos: {mais_50}")



#um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares. Mostre uma mensagem caso o valor não seja válido e continue pedindo até que o usuário informe, ao total, os 10 valores válidos
pares = 0
impares = 0
contador = 0
while contador < 10:
    numero = int(input("Digite um número inteiro:" ))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1 
        contador +=1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")



#um programa que leia a idade da pessoa, a quantidade e a categoria do ingresso a ser comprado, mostrando o valor do ingresso considerando: Categoria A – R$40,00 / Categoria B – R$30,00 / Categoria C – R$25,00. Caso a pessoa tenha idade a partir de 60 anos, deverá ser cobrada apenas a metade do valor do ingresso. O sistema deverá exibir o valor a ser pago, e perguntar se deseja continuar comprando ingresso e o usuário deve responder Sim ou Não
continuar = "sim"

while continuar == "sim":
    idade = int(input("Digite sua idade: "))
    quantidade = int(input("Digite a quantidade de ingressos: "))
    categoria = input("Digite a categoria do ingresso (A, B ou C): ").upper()

    if categoria == "A":
        valor_unitario = 40.0
    elif categoria == "B":
        valor_unitario = 30.0
    elif categoria == "C":
        valor_unitario = 25.0
    else:
        print("Categoria inválida!")
        continue

    if idade >= 60:
        valor_unitario /= 2

    valor_total = quantidade * valor_unitario
    print(f"Valor a ser pago: R${valor_total:.2f}")

    continuar = input("Deseja continuar comprando ingressos? (Sim/Não): ")

print("Compra finalizada. Obrigado!")
