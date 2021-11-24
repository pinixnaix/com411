import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    print(frame)


def run():
    global fig
    some_animation = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()


if __name__ == '__main__':
    run()
