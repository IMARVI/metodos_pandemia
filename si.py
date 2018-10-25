import matplotlib.pyplot as plt

# poblacion
N = 7_500_000_000
# numero de infectrados
I = 10_000
# suceptibles a infectarse
S = N - I
# probabilidad de que se infecten
beta = 0.009
# susceptibles
sus = []

# infectados
inf = []  

# probabilidad en tiempo T
prob = []

# metodo sis basado en el modelo
def si(S, I, N):
    t = 0
    while (t < 2000):
        S, I = S - beta * (S * I / N), I + beta * ((S * I) / N)
        p = beta * (I / N)

        sus.append(S)
        inf.append(I)
        prob.append(p)
        t = t + 1


si(S, I, N)
figure = plt.figure()
figure.canvas.set_window_title('Modelo SI')
figure.add_subplot(211)
inf_line, =plt.plot(inf, label='I(t)')
sus_line, = plt.plot(sus, label='S(t)')
plt.legend(handles=[inf_line, sus_line])
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax = figure.add_subplot(212)
prob_line = plt.plot(prob, label='p(t)')
plt.legend(handles=prob_line)
type(ax)
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])
plt.xlabel('T')
plt.ylabel('p')
plt.show()