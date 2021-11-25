import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

fig, ax = plt.subplots()


def animate(frame):
    global ax
    ax.set_xlim(frame/2, 720+frame)
    ax.set_ylim(-1, 1)
    x = range(0, frame)
    y = [math.sin(math.radians(degrees)) for degrees in x]
    ax.plot(x, y)


def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=720, interval=100)
    plt.show()


run()
