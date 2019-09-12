import matplotlib.pyplot as plt

tigers = [529, 190, 28, 88]
states = ['Karnataka', 'Kerala',
          'Odisha', 'West Bengal']

# Define a label to be used in legend.
plt.bar(states, tigers, label='tigers')

plt.xlabel('State')
plt.ylabel('Population')
plt.title('Wildlife Population in 2019')

# Place a legend.
plt.legend()

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
