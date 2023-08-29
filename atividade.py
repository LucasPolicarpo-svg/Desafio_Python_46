import math  # aqui faz a importação do math para fazer o calculo.

def calc_bask(a, b, c):
    delta = b**2 - 4*a*c

# condições para que o calculo seja feito de forma correta.
    if delta < 0:
        return "Não existe raízes reais"
    elif delta == 0:
        raiz = -b /(2*a)
        return f"A equação possui uma raiz real: {raiz:.2f}"
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return f"A equação possui duas raiz real: {raiz1:.2f} e {raiz2:.2f}"


# Para adicionar os valores dos coeficientes a,b,c.

a = float(input("Digite o valor do coeficiente A:"))
b = float(input("Digite o valor do coeficiente B:"))
c = float(input("Digite o valor do coeficiente C:"))

# Agora chamamos a função para exibir o resultado

resultado = calc_bask(a, b, c)
print(resultado)