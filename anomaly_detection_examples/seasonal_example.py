from tools.my_plots import anomalies_scatters_two_plots
from diss_functions.diss_metric import diss_metric
import pandas as pd
import numpy as np
import math
import random

def seasonal_example():
    label = 'Simple Seasonal Anomaly Detection (Standart Metric)'
    window_size = 20
    error_range = range(650, 750)
    anomalies: list = []
    n = 1000
    const = 20
    error = 20
    coef_param = 1
    threshold = 0.5
    #time_shift = 5

    for time_shift in range(1,20,1):

        period: list = list(range(n))
        baseline: list = [const + math.sin(0.05*i) for i in range(n)]
        data: list = [value for value in baseline]

        #seasonal_error_end = baseline[800]

        for error_index in error_range:
            data[error_index] = error

        example_ts = pd.DataFrame()
        example_ts['time'] = period[:n-time_shift]
        example_ts['expected'] = baseline[:n-time_shift]
        example_ts['actual'] = data[time_shift:]

        diss_results = diss_metric(example_ts, 'time', threshold)

        # get time points from diss_results
        #anomalies = [diss[0] for diss in diss_result]

        #print(anomalies)
        anomalies_scatters_two_plots(example_ts['time'], example_ts['expected'], example_ts['actual'], label, diss_results,
                                     time_shift)


if __name__ == '__main__':
    seasonal_example()