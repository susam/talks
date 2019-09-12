import matplotlib.pyplot as plt

# Format string:
#   'o' for circle marker.
#   '-' for solid line.
plt.plot([2, 3, 5, 7, 11], 'o-')

plt.xlabel('index')
plt.ylabel('prime number')
plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
