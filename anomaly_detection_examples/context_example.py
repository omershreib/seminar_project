from tools.my_plots import anomalies_scatters_plot
import numpy as np
import math
import random

def context_example():
    label = 'Simple Contextual Anomaly Detection'
    window_size = 20
    spikes: list = [10, 20, 60, 80]
    anomalies: list = []
    n = 100
    const = 20
    error = 10
    coef_param = 1
    threshold = lambda window, param: param*np.var(window)

    period: list = list(range(n))
    baseline: list = [max(const + math.sin(i), const) for i in range(n)]
    data: list = [value for value in baseline]

    # add noise errors
    for spike in spikes:
        data[spike] +=  error * random.random()

    # detect contextual anomalies
    for i in range(0,n-window_size):
        anomalies_in_curr_windows = []
        current_time_window = range(i, i+window_size)
        current_window = data[i: i+window_size]
        current_threshold = threshold(current_window, coef_param)

        for t in current_time_window:
            result = abs(data[t] - baseline[t])

            if result > current_threshold:
                if t not in anomalies:
                    anomalies.append(t)

    anomalies_scatters_plot(period, data, label, anomalies)


if __name__ == '__main__':
    context_example()