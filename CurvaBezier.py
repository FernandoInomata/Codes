#Para exercicio 2 CG () - Lista 3  
#Curva de Bezier - Cúbica
def calcular_P(t, P1, P2, P3, P4):
    calc1 = ((1-t)**3) * P1
    calc2 = 3*(1-t)**2 * t * P2
    calc3 = 3*(1-t)* t**2 * P3
    calc4 = t**3 * P4

#    Mostrar o valor de cada calculo    
    #print ("Calc1: ",calc1)
    #print ("Calc2: ",calc2)
    #print ("Calc3: ",calc3)
    #print ("Calc4: ",calc4)

    P = calc1 + calc2 + calc3 + calc4
    return P

# Alterar esses valores
t = 1
P1 = 19
P2 = -5
P3 = 20
P4 = 11

resultado = calcular_P(t, P1, P2, P3, P4)
print(f"P({t}) = {resultado:.5f}")
