import matplotlib.pyplot as plt

# Data: Number of successfully received packets
received_packets = [
    25, 26, 28, 30, 38, 38, 38, 39, 43, 48, 46, 57, 60, 24, 23, 19, 19, 19,
    20, 21, 22, 44, 22, 21, 12, 12, 12, 22, 22, 16, 15, 26, 26, 26, 26, 27,
    27, 28, 31, 32, 35, 35, 36, 25, 23, 21, 20, 19, 21, 22, 21, 20, 20, 20,
    15, 11, 12, 22, 17, 16, 16, 0, 0, 0, 0, 0, 0, 0
]

# Data: Number of packets sent by source vehicle
sent_packets = [
    25, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0
]

# Calculating PDR
pdr = []
for received, sent in zip(received_packets, sent_packets):
    if sent != 0:
        pdr.append(received / sent)
    else:
        pdr.append(0)  # Avoid division by zero

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(pdr, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Vehicles')
plt.ylabel('Packet Delivery Ratio (PDR)')
plt.title('')
plt.grid(True)
plt.show()