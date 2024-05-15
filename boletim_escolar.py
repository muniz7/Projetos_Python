#import tkinter
bol = "Bem vindo ao boletim escolar"
print(bol)


n1 = float(input("Digite a primeira nota: "))

n2 = float(input("Digite a segunda nota: "))

n3 = float(input("Digite a terceira nota: "))

n4 = float(input("Digite a quarta nota: "))

result = ((n1 + n2 +n3 + n4)/4)
print(" A media foi: ", f"{result:.1f}")


if result >= 6:
    print("aprovado")
else:
    print("reprovado")
