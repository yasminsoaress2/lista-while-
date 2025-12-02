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