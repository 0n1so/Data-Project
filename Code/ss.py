import matplotlib.pyplot as plt
import numpy as np

x = np.array(['10:00', '12:00', '14:00', '16:00', '18:00', '20:00'])

y1 = np.array([230, 212, 77, 97, 560, 877])
y2 = np.array([450, 660, 321, 210, 1100, 1692])
y3 = np.array([900, 1020, 567, 430, 320, 205])

libriya_func = dict(marker = '.',
                    markersize = 15,
                    markerfacecolor = "#ECECEC",
                    markeredgecolor = "#4b4b4b",
                    linestyle = 'dashed',
                    linewidth = 4)

plt.plot(x, y1, color = '#230f5c', **libriya_func)
plt.plot(x, y2, color = '#8a0411', **libriya_func)
plt.plot(x, y3, color = '#3cde14', **libriya_func)

plt.show()