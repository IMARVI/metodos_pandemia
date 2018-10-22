import matplotlib.pyplot as plt

N = 7_500_000_000
I = 1
S = N - I
beta = 0.19

sus = []  # susceptible compartment
inf = []  # infected compartment
prob = []  # probability of si at time t


def si(S, I, N):
    t = 0
    while (t < 500):
        S, I = S - beta * (S * I / N), I + beta * ((S * I) / N)
        p = beta * (I / N)

        sus.append(S)
        inf.append(I)
        prob.append(p)
        t = t + 1


si(S, I, N)
print(inf)
figure = plt.figure()
figure.canvas.set_window_title('SI model')

figure.add_subplot(211)
inf_line, =plt.plot(inf, label='I(t)')

sus_line, = plt.plot(sus, label='S(t)')

plt.legend(handles=[inf_line, sus_line])

plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0)) # use scientific notation

ax = figure.add_subplot(212)
prob_line = plt.plot(prob, label='p(t)')
plt.legend(handles=prob_line)

type(ax)  # matplotlib.axes._subplots.AxesSubplot

# manipulate
vals = ax.get_yticks()
ax.set_yticklabels(['{:3.2f}%'.format(x*100) for x in vals])

plt.xlabel('T')
plt.ylabel('p')

plt.show()