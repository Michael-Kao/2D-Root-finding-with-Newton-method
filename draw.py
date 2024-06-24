import numpy as np
import matplotlib.pyplot as plt
from numpy import arange, meshgrid, sqrt

# p1 = [-2.9999, -1.99997, -1.75, -1.73214, -1.73205, -1.73205]
# p2 = [-2.9999, -1.66662, -1.13332, -1.00784, -1.00003, -1]

colorMap = {}
colorUsed = {}

def read_data():
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    xlist = []
    ylist = []
    x = []
    y = []
    f = open("result.txt")
    for line in f:
        if line[0] == '-' and x and y:
            key = (x[-1], y[-1])
            if len(x) > 1:
                colorMap[key] = np.random.uniform(low=0.5, high=0.85, size=(3, ))
            else:
                colorMap[key] = 'k'
            colorUsed[key] = False
            xlist.append(x)
            ylist.append(y)
            x = []
            y = []
        if line[0] not in num:
            continue
        temp = line.split(" : ")
        num_str = temp[1].strip("()\n")
        numlist = num_str.split(',')
        x.append(float(numlist[0]))
        y.append(float(numlist[1]))
    return xlist, ylist

def draw():
    delta = 0.025
    x, y = meshgrid(
        arange(-5, 5, delta),
        arange(-5, 5, delta)
    )

    plt.contour(
        x, y,
        x ** 2 + y ** 2 - 4,
        [0]
    )

    x, y = meshgrid(
        arange(-5, 5, delta),
        arange(-5, 5, delta)
    )

    plt.contour(
        x, y,
        x ** 2 - y ** 2 - 2,
        [0]
    )

    # fig, ax = plt.subplots(7, 7)

    xdata, ydata = read_data()
    for i in range(len(xdata)):
        key = (xdata[i][-1], ydata[i][-1])
        color = colorMap[key]
        if not colorUsed[key] and type(color) != type("str"):
            colorUsed[key] = True
            Label = key
        else:
            Label = None
        if xdata[i][0] == -1.9999 and ydata[i][0] == 0.0001:
            plt.plot(xdata[i], ydata[i], c=color, marker='o', linestyle = 'dashed', label=Label)
        # else:
        #     plt.plot(xdata[i][0], ydata[i][0], c=color, marker='o', linestyle = 'dashed', label=Label)
    # plt.plot(p1, p2, '.:g')

    plt.legend(labelcolor='linecolor')
    plt.grid()
    plt.show()

draw()