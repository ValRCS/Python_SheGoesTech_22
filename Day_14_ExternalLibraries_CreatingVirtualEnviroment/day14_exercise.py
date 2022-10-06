# TODO
# 1. plot a graph of x and y
# x would be values from -10 to 10 (21 values)
# y would be the cube of x + 5

# you could use a different library than matplotlib but it is the most popular one
# will will explore other ones later on in the course

# from  matplotlib import pyplot as plt

# what plot styles are available?
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
# plt.style.use('seaborn')
# plt.style.use('ggplot')
# plt.style.use('fivethirtyeight')
# plt.style.use('dark_background')
# plt.style.use('bmh')
# plt.style.use('classic')
# plt.style.use('Solarize_Light2')
# plt.style.use('tableau-colorblind10')
# plt.style.use('fast')
# plt.style.use('grayscale')
# plt.style.use('seaborn-whitegrid')
# plt.style.use('seaborn-darkgrid')
# plt.style.use('seaborn-notebook')
# plt.style.use('seaborn-ticks')
# plt.style.use('seaborn-poster')
# plt.style.use('seaborn-talk')


# plt.style.use('_mpl-gallery')

# x = list(range(-10, 11))
# y = [i**3+5 for i in x]
# fig, ax = plt.subplots()
# ax.scatter(x, y)
# plt.savefig("mygraph.png")
# plt.show()

# create matlplotlib animation of a sine wave
# https://matplotlib.org/stable/gallery/animation/simple_anim.html
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig, ax = plt.subplots()
# x = np.arange(0, 2*np.pi, 0.01)        # x-array
# ax.plot(x, np.sin(x))

# plt.show()

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')


# make data
x = [1, 4, 2, 2]
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))

# plot
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 3, "edgecolor": "red"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()
