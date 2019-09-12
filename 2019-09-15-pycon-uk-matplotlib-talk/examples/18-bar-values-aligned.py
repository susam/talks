import matplotlib.pyplot as plt

tigers = [529, 190, 28, 88]
states = ['Karnataka', 'Kerala',
          'Odisha', 'West Bengal']

plt.bar(states, tigers, label='tigers')

plt.xlabel('State')
plt.ylabel('Population')
plt.title('Wildlife Population in 2019')
plt.legend()

for index, value in enumerate(tigers):
    plt.text(index, value + 5, value, ha='center')

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
