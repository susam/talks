import matplotlib.pyplot as plt

plt.plot([2, 3, 5, 7, 11], 'o-')
plt.xlabel('index')
plt.ylabel('prime number')

# Place ticks at integer positions.
plt.xticks(range(5))
plt.yticks(range(2, 12))

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
