import matplotlib.pyplot as plt
import numpy as np


mu, sigma = 0, 0.1  # mean and standard deviation
s = np.random.normal(0, 0.1, 100)
ss = np.random.normal(0, 0.1, 500)
sss = np.random.normal(0, 0.1, 2000)
fig, ax = plt.subplots(1, 3)

# высота, координата и...
count, bins, ignored = ax[0].hist(s, 30, density=True)
count, bins, ignored = ax[1].hist(ss, 30, density=True)
count, bins, ignored = ax[2].hist(sss, 30, density=True)
print(ignored)

ax[0].plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
           np.exp(- (bins - mu)**2 / (2 * sigma**2)),
           linewidth=2, color='r')
ax[1].plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
           np.exp(- (bins - mu)**2 / (2 * sigma**2)),
           linewidth=2, color='r')
ax[2].plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
           np.exp(- (bins - mu)**2 / (2 * sigma**2)),
           linewidth=2, color='r')


plt.show()
