#Este programa lo que hará será mostrar la expresión matemática simbólica de Vc(t)
#Además hará una gráfica que mostrará como el voltaje del capacitor va creciendoe exponencialmente hasta 21
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Parámetros del circuito
E = 21.0  # Voltaje de la fuente :,v
R1 = 60000.0  # todas las medaidas de R están en ohms
R2 = 30000.0  
R3 = 10000.0  
C = 0.2e-6    # eto ta en faradios 

# Sabemos que el cáculo de resistencia equivalente: Req = (R1 || R2) + R3
R_paralelo = (R1 * R2) / (R1 + R2)
Req = R_paralelo + R3
tau = Req * C  # esta es la constante de tiempo 

# a continuación estan las expresiones simbolicas para mostrar con sympy
t = sp.symbols('t', real=True, positive=True)
vC_expr = E * (1 - sp.exp(-t / tau))
print("Expresión simbólica de vC(t):")
sp.pprint(vC_expr, use_unicode=True)

# Esto es para generar datos para graficar vC(t)
t_vals = np.linspace(0, 5 * tau, 500)
vC_vals = E * (1 - np.exp(-t_vals / tau))

#Esto sería para la gráfica
plt.figure(figsize=(8, 5))
plt.plot(t_vals, vC_vals, label=r'$v_C(t) = 21(1 - e^{-t/\tau})$', color='blue')
plt.axhline(y=E, color='gray', linestyle='--', linewidth=0.7, label=f'Voltaje Final :D ({E} V)')
plt.title("Carga del Capacitor vC(t)  :)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje vC (V) :p")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
