import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy as np

# poblacion
N = 7_500_000_000
# numero de infectados
I = 1
# suceptibles a infeccion
S = N - I
# recuperados
R = 0
# tasa de infeccion
beta = 0.3 
# tasa de recuperacion
gamma = 0.05


def diff(sir, t):
    # sir[0] - S, sir[1] - I, sir[2] - R
    dsdt = - (beta * sir[0] * sir[1])/N
    didt = (beta * sir[0] * sir[1])/N - gamma * sir[1]
    drdt = gamma * sir[1]
    dsirdt = [dsdt, didt, drdt]
    return dsirdt

# Condiciones iniciales
iniciales = (S, I, R)

# graficamos puntos
t = np.linspace(0, 100)

sir = odeint(diff, iniciales, t)

plt.plot(t, sir[:, 0], label='S(t)')
plt.plot(t, sir[:, 1], label='I(t)')
plt.plot(t, sir[:, 2], label='R(t)')

plt.legend()

plt.xlabel('T')
plt.ylabel('N')

# use scientific notation
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.show()