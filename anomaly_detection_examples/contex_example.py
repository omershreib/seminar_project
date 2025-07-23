from tools.global_detect_plot import global_detect_plot
import numpy as np
import math
import random

def apx_close_to_threshold(result, threshold, epsilon = 0.1):
    return abs(result - threshold) < epsilon

def main():
    label = 'Simple Contextual Anomaly Detection'
    window_size = 10
    spikes: list = [10, 20, 60, 80]
    anomalies: list = []
    n = 100
    const = 20
    error = 10
    coef_param = 1
    threshold = lambda window, param: param*np.var(window)

    period: list = list(range(n))
    baseline: list = [const + math.sin(i) for i in range(n)]
    data: list = []


    for i, value in enumerate(baseline):
        if value < const:
            baseline[i] = const


    # add errors
    for i in range(n):
        data.append(baseline[i])

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

            if t in spikes:
                print(t, result, current_threshold)

            if result > current_threshold:
                if t not in anomalies:
                    anomalies.append(t)


    global_detect_plot(period, data, label, anomalies)


if __name__ == '__main__':
    main()