import matplotlib.pyplot as plt
import numpy as np

tigers = [529, 190, 28, 88]
elephants = [6049, 5706, 1976, 194]
states = ['Karnataka', 'Kerala',
          'Odisha', 'West Bengal']

indices = np.arange(len(states))
w = 0.3  # Width of each bar

plt.bar(indices - w / 2, tigers, w, label='Tigers')
plt.bar(indices + w / 2, elephants, w, label='Elephants')

plt.xlabel('State')
plt.ylabel('Population')
plt.title('Wildlife Population in 2019')
plt.legend()

plt.xticks(indices, states)

for index, value in enumerate(tigers):
    plt.text(index - w / 2, value + 30, value, ha='center')

for index, value in enumerate(elephants):
    plt.text(index + w / 2, value + 30, value, ha='center')

plt.savefig('out.png', dpi=300, bbox_inches='tight')
