import matplotlib.pylab as plt
from scipy.integrate import odeint
import numpy as np

N = 7_500_000_000
I = 1
S = N - I
R = 0
beta = 0.3  # infection rate
gamma = 0.05  # recovery rate


def diff(sir, t):
    # sir[0] - S, sir[1] - I, sir[2] - R
    dsdt = - (beta * sir[0] * sir[1])/N
    didt = (beta * sir[0] * sir[1])/N - gamma * sir[1]
    drdt = gamma * sir[1]
    print (dsdt + didt + drdt)
    dsirdt = [dsdt, didt, drdt]
    return dsirdt


# initial conditions
sir0 = (S, I, R)

# time points
t = np.linspace(0, 100)

# solve ODE
# the parameters are, the equations, initial conditions,
# and time steps (between 0 and 100)
sir = odeint(diff, sir0, t)

plt.plot(t, sir[:, 0], label='S(t)')
plt.plot(t, sir[:, 1], label='I(t)')
plt.plot(t, sir[:, 2], label='R(t)')

plt.legend()

plt.xlabel('T')
plt.ylabel('N')

# use scientific notation
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.show()