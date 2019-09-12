import matplotlib.pyplot as plt

logs = [1000, 2000, 3000, 4000,
        5000, 6000, 7000, 8000]

time = [1, 3, 43, 97, 218, 273,
        368, 520]

plt.plot(logs, time, 'o-')
plt.xlabel('Chunk size (log count)')
plt.ylabel('Time consumed (seconds)')

plt.savefig('out.png', dpi=300,
            bbox_inches='tight')
