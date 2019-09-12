import matplotlib.pyplot as plt

# 'v' for triangle down marker
plt.plot([2, 3, 5, 7, 11], 'v')
plt.xlabel('index')
plt.ylabel('prime number')

plt.xticks(range(5))
plt.yticks(range(2, 12))

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
