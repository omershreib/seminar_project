from tools.my_plots import anomalies_scatters_plot
from tools.coin import coin
import random
import numpy as np
import pandas as pd
import math


def global_example():
    label = 'Simple Global Anomaly Detection'
    spikes: list = [10,20,50,70]
    anomalies: list = []
    n = 100
    const = 20
    error = 10
    threshold = 5

    period: list = list(range(n))
    data: list = [max(const + math.sin(i), const) for i in range(n)]

    for spike in spikes:
        value = data[spike]
        data[spike] += error*random.random()

        # detect global anomalies
        print(data[spike], value, threshold)
        if abs(data[spike] - value) > threshold:
            anomalies.append(spike)

    anomalies_scatters_plot(period, data, label, anomalies)



if __name__ == '__main__':
    global_example()