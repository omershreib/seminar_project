from tools.global_detect_plot import global_detect_plot
from tools.coin import coin
import random
import numpy as np
import pandas as pd
import math


def main():
    label = 'Simple Global Anomaly Detection'
    spikes: list = [10,20,50,70]
    anomalies: list = []
    n = 100
    const = 20
    error = 10
    threshold = 5

    period: list = list(range(n))
    #pred: list = [const for i in range(n)]
    data: list = [const + math.sin(i) for i in range(n)]

    for i, value in enumerate(data):
        if value < const:
            data[i] = const


    for spike in spikes:
        value = data[spike]
        data[spike] += error*random.random()

        # detect global anomalies
        print(data[spike], value, threshold)
        if abs(data[spike] - value) > threshold:
            anomalies.append(spike)


    global_detect_plot(period, data, label, anomalies)



if __name__ == '__main__':
    main()