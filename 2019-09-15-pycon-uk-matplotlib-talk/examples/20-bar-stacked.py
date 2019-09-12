import matplotlib.pyplot as plt

tigers = [529, 190, 28, 88]
elephants = [6049, 5706, 1976, 194]
states = ['Karnataka', 'Kerala',
          'Odisha', 'West Bengal']

plt.bar(states, tigers, label='tigers')
plt.bar(states, elephants, label='elephants',
        bottom=tigers)

plt.xlabel('State')
plt.ylabel('Population')
plt.title('Wildlife Population in 2019')
plt.legend()

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
