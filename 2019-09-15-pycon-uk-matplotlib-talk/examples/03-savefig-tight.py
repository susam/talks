import matplotlib.pyplot as plt

plt.plot([2, 3, 5, 7, 11])
plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
