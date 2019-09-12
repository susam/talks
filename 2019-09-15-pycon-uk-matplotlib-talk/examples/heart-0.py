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

plt.savefig('out.png', dpi=300, bbox_inches='tight')

# pylama:ignore=W0611
