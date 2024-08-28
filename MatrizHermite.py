#Para exercicio 1 CG () - Lista 3  

def calcular_P(t, P1, P2, T0, T1):
    calc1 = (2 * t**3 - 3 * t**2 + 1) * P1
    calc2 = (-2 * t**3 + 3 * t**2) * P2
    calc3 = (t**3 - 2 * t**2 + t) * T0
    calc4 = (t**3 - t**2) * T1

#    Mostrar o valor de cada calculo    
    print ("Calc1: ",calc1)
    print ("Calc2: ",calc2)
    print ("Calc3: ",calc3)
    print ("Calc4: ",calc4)

    P = calc1 + calc2 + calc3 + calc4
    return P

# Alterar esses valores
t = 0.9
P1 = 20
P2 = 5
T0 = 8
T1 = -3

resultado = calcular_P(t, P1, P2, T0, T1)
print(f"P({t}) = {resultado:.5f}")
