import matplotlib.pyplot as plt
import numpy as np
X = [[1,2],[3,4]]



np.random.seed(19680801)
data = np.random.randn(2, 100)
plt.style.use('seaborn')  # ['seaborn-ticks', 'ggplot', 'dark_background', 'bmh', 'seaborn-poster', 'seaborn-notebook', 'fast', 'seaborn', 'classic', 'Solarize_Light2', 'seaborn-dark', 'seaborn-pastel', 'seaborn-muted', '_classic_test', 'seaborn-paper', 'seaborn-colorblind', 'seaborn-bright', 'seaborn-talk', 'seaborn-dark-palette', 'tableau-colorblind10', 'seaborn-darkgrid', 'seaborn-whitegrid', 'fivethirtyeight', 'grayscale', 'seaborn-white', 'seaborn-deep']
plt.figure.title = 'Company evenue'
fig, axs = plt.subplots(2, 3, figsize=(6, 6))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])
axs[0, 2].pie(data[0])
axs[1, 2].bar([2,3,4],[2,3,1])
axs[1,1].set(xlim=[-1, 4], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
labels = axs[1, 2].get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
plt.show()


