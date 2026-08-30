import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def rotate(theta):
    V = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta),  np.cos(theta)]])
    return V

fig, ax = plt.subplots()

def draw_frame(i):
    ax.clear()
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.axis('equal')
    theta = 2 * np.pi * i / 120
    R = rotate(theta)

    i_hat = np.array([1., 0.])
    j_hat = np.array([0., 1.])

    new_i = R @ i_hat
    new_j = R @ j_hat

    ax.arrow(0, 0, new_i[0], new_i[1], head_width=0.1, color='tab:red')
    ax.arrow(0, 0, new_j[0], new_j[1], head_width=0.1, color='tab:blue')

    t = np.linspace(-3, 3, 100)
    k = np.linspace(-3, 3, 7)
    for k_ in k:
        line = np.column_stack([t, np.full(100, k_)])
        new_line = R @ line.T
        ax.plot(new_line[0, :], new_line[1, :], color='gray', lw=0.5)
    for k_ in k:
            line = np.column_stack([np.full(100, k_), t])
            new_line = R @ line.T
            ax.plot(new_line[0, :], new_line[1, :], color='gray', lw=0.5)

anim = FuncAnimation(fig, draw_frame, frames=120, interval=40)
anim.save('week01/rotation.gif', writer='pillow', fps=25)