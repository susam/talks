import matplotlib.pyplot as plt

plt.plot([2, 3, 5, 7, 11])

# Label x-axis and y-axis.
plt.xlabel('index')
plt.ylabel('prime number')

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
