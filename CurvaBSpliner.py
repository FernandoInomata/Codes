def Bspline_CalcN(t):
    N0 = (1 - t)**3 / 6
    N1 = (3 * t**3 - 6 * t**2 + 4) / 6
    N2 = (-3 * t**3 + 3 * t**2 + 3 * t + 1) / 6
    N3 = t**3 / 6
    #print("N0 = ", N0)
    #print("N1 = ", N1)
    #print("N2 = ", N2)
    #print("N3 = ", N3)

    return N0, N1, N2, N3

def calcular_bspline(t, P1, P2, P3, P4):
    N0, N1, N2, N3 = Bspline_CalcN(t)
    
    # Cálculo das coordenadas x, y e z
    x = N0 * P1 + N1 * P2 + N2 * P3 + N3 * P4
    
    return x

# Alterar esses valores
t = 0.94
P1 = 8
P2 = 12
P3 = -4
P4 = 7

resultado = calcular_bspline(t, P1, P2, P3, P4)
print(f"P({t}) = {resultado}")
