import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

label_for_legend = (
    r'$y_1 = \sqrt{1 - |x|} \sqrt{|x|}$, '
    r'$y_2 = -\frac{3}{2} \sqrt{1 - \sqrt{|x|}}$'
)

x = np.linspace(-1, 1, 10001)
y1 = np.sqrt(1 - np.abs(x)) * np.sqrt(np.abs(x))
y2 = (-3 / 2) * np.sqrt(1 - np.sqrt((np.abs(x))))

plt.plot(x, y1, 'r', label=label_for_legend)
plt.plot(x, y2, 'r')
plt.legend(shadow=True)

# Set wider x-limit and y-limit.
plt.xlim([-1.5, 1.5])
plt.ylim([-1.6, 1.0])

ax = plt.gca()

# Set major and minor tick loations on the axes.
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(0.1))

plt.savefig('out.png', dpi=300, bbox_inches='tight')
