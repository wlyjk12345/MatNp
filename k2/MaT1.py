import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()  # an empty figure with no axes                背景
fig.suptitle('No axes on this figure')  # Add a title so we know which it is
fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

x = np.linspace(0, 2, 100)
# color label width line
plt.plot(x, x,   x, x**4, label='linear',color="blue", linewidth=0.25)
plt.plot(x, x**2, label='quadratic',lw=2, linestyle='-',marker='o', markersize=5, markerfacecolor="red")  # possible linestype options ‘-‘, ‘–’, ‘-.’, ‘:’, ‘steps’
plt.plot(x, x**3, label='cubic',lw=2, ls='-.')   # possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
plt.legend(loc=1) #      #加入图例          http://matplotlib.org/users/legend_guide.html#legend-location
#   loc图例的位置  1 upper right corner    2 upper left corner  3 lower left corner 4 lower right corner

#plt.plot(x,y[x])

plt.xlabel('x label')
plt.ylabel('y label')
plt.ylim([0, 5])
plt.axis([0, 6, 0, 4])   #[xmin, xmax, ymin, ymax]
plt.grid(True) #(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)


#plt.yscale("log")
plt.title("Simple Plot",fontsize=6)


fig, ax_lst = plt.subplots(2, 3, sharex='none', sharey='none')  # a figure with a 2x2 grid of Axes
data1, data2, data3, data4 = np.random.randn(4, 100)      #  1.True或者'all'：x或y轴属性将在所有子图(subplots)中共享.False或'none'：每个子图的x或y轴都是独立的部分'row'：每个子图在一个x或y轴共享行(row).'col':每个子图在一个x或y轴共享列(column)
#plt.grid(True)

plt.plot(data1, data2)
ax_lst[0, 0].plot(data3, data4)
ax_lst[0, 1].plot(data1, data2)
#ax_lst[1, 0].plot([1, 2, 3, 4], [1, 4, 9, 16])
a = ax_lst[1, 0].imshow([[1,2],[3,4],[5,6]],cmap=plt.cm.autumn, interpolation='nearest')
plt.colorbar(a)
#fig.savefig("filename.png", dpi=200) #saving

plt.show()