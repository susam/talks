import matplotlib.pyplot as plt

tigers = [529, 190, 28, 88]
states = ['Karnataka', 'Kerala',
          'Odisha', 'West Bengal']

plt.bar(states, tigers)

plt.xlabel('State')
plt.ylabel('Population')
plt.title('Wildlife Population in 2019')

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
