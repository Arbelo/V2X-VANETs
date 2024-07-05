


import matplotlib.pyplot as plt


busy_time = [
    3.71E-05, 5.48E-05, 5.56E-05, 5.65E-05, 5.74E-05, 5.83E-05, 6.05E-05, 6.28E-05,
    7.04E-05, 7.42E-05, 7.55E-05, 8.24E-05, 8.67E-05, 3.70E-05, 3.34E-05, 3.10E-05,
    3.01E-05, 3.07E-05, 3.45E-05, 3.68E-05, 3.92E-05, 7.51E-05, 3.75E-05, 3.66E-05,
    2.14E-05, 2.19E-05, 2.43E-05, 4.60E-05, 5.70E-05, 6.25E-05, 5.59E-05, 5.53E-05,
    5.91E-05, 6.08E-05, 6.26E-05, 6.46E-05, 6.91E-05, 7.14E-05, 8.17E-05, 8.73E-05,
    9.90E-05, 1.03E-04, 1.10E-04, 7.95E-05, 7.95E-05, 7.27E-05, 7.25E-05, 7.99E-05,
    8.40E-05, 9.28E-05, 9.37E-05, 9.47E-05, 1.01E-04, 1.08E-04, 9.28E-05, 7.52E-05,
    8.19E-05, 1.95E-04, 2.49E-04, 2.97E-04, 2.95E-04, 1.22E-05, 0, 0, 0, 0, 0, 0
]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(busy_time, marker='o', linestyle='-', color='b')
plt.title('Vehicle Busy Time', va='bottom', ha='center')
plt.xlabel('Number of Vehicles')
plt.ylabel('Busy Time (seconds)')
plt.grid(True)
plt.show()