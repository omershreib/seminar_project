import matplotlib.pyplot as plt
import numpy as np


def global_detect_plot(period, data:list, label, anomalies=None):
    plt.figure(figsize=(10,6))
    plt.plot(period, data, label='data plot', color='red')
    plt.xlabel('Period')
    plt.ylabel('Data')
    plt.title(label)


    y_anomalies = []

    for point in anomalies:
        y_anomalies.append(data[point])

    plt.scatter(anomalies, y_anomalies, label='anomalies', color='blue', marker='x', s=100)

    plt.legend()
    plt.show()