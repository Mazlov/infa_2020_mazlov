import matplotlib.pyplot as plt
import numpy as np

x = [0.459, 0.539, 0.882, 1.064, 1.096, 1.400, 1.421, 1.715, 2.131, 2.763]
y = [0.559, 0.712, 0.754, 0.955, 0.913, 1.255, 1.199, 1.606, 1.949, 2.454]
p, v = np.polyfit(x, y, deg=1, cov=True)
plt.errorbar(x, y, xerr=0.05, yerr=0.1, linestyle=offset)
f = np.poly1d(p)
plt.plot(x, f(x))
plt.grid()
plt.show()