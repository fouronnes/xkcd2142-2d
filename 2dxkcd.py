from matplotlib import pyplot as plt
import numpy as np

plt.xkcd()

data = np.array([
    [26, 0],
    [36, 990],
    [42, 250],
    [48, 25],
    [103, 15],
    [123, 5],
    [182, 315],
    [192, 20],
    [233, 270],
    [691, 35]
])

fields = [
    "MATHEMATICS",
    "ASTRONOMY",
    "ECONOMICS",
    "LAW",
    "CRIMINOLOGY",
    "METEOROLOGY",
    "CHEMISTRY",
    "MARINE BIOLOGY",
    "VOLCANOLOGY",
    "GERONTOLOGY",
]

xytexts = np.array([
    [10,  160],
    [30, 800],
    [12, 350],
    [70, 60],
    [123,  120],
    [143,   60],
    [202, 315],
    [270,  20],
    [253, 270],
    [600,  90]
])


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(1, 1, 1)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.xticks([])
plt.yticks([])

ax.set_xlim([0, 750])
ax.set_ylim([-10, 1050])

plt.xlabel("PROBABILITY THAT YOU'LL BE KILLED\nBY THE THING YOU STUDY - BY FIELD")
plt.ylabel("PROBABILITY OF YOUR SPECIES BEING\nWIPED OUT BY SAID FIELD")

for field, xytext, xy in zip(fields, xytexts, data):
    plt.annotate(field, xy=xy, arrowprops=dict(arrowstyle='-', shrinkB=6), xytext=xytext)

plt.plot(data[:, 0], data[:, 1], linestyle="", marker=".", color="k", markersize=10)


plt.show()


