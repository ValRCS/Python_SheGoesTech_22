import matplotlib.pyplot as plt
# import numpy as np

plt.style.use('_mpl-gallery')

# make data
# x = np.linspace(0, 10, 100)
# y = 4 + 2 * np.sin(2 * x)
# x and y could be lists of values
x = list(range(0, 10))
y = [n**2 for n in x]

# plot
fig, ax = plt.subplots()

ax.plot(x, y, linewidth=2.0)


plt.show()