from matplotlib.dates import MonthLocator, DateFormatter, YearLocator
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random



def load_calit2_data(filepath):
    df = pd.read_csv(filepath, names=['flow_id', 'date', 'time', 'people'])
    flow_in = df[df.flow_id == 9][['date', 'time', 'people']]    # flow_id = 9
    flow_out = df[df.flow_id == 7][['date', 'time', 'people']]   # flow_id = 7

    return flow_in, flow_out


def create_time_sequence(data):
    seq = []
    period = []
    period_format = '{} {}'

    for i, row in data.iterrows():
        #print(row)
        date_value = row['date']
        time_value = row['time']
        people_value = row['people']

        #print(period_format.format(date_value, time_value))
        #exit()

        period.append(period_format.format(date_value, time_value))
        seq.append(people_value)

    return  np.array(seq), np.array(period)


def generate_period(n):
    return np.array(list(range(n)))


def coin():
    return random.random() > 0.5


def generate_random_sequence(n, start, stop, instability):
    points = []
    baseline = (start + stop)/2
    pick = 5

    for _ in range(n):

        if random.random() > instability:
            points.append(baseline)
        else:
            #points.append(random.randrange(start,stop,1))
            if coin():
                points.append(baseline + pick)

            else:
                points.append(baseline - pick)

    return np.array(points)



def diss(x,y):
    return abs(x-y)


def plot(seq_1, seq_2, period):

    period = pd.to_datetime(period)
    fig, (ax1, ax2) = plt.subplots(2, 1)
    fig.suptitle('Calit2 In/Out Flow Over Time')

    ax1.plot(period, seq_1, '.-')
    ax2.plot(period, seq_2, '.-')
    ax1.set_ylabel('In')

    ax2.set_xlabel('time (s)')
    ax2.set_ylabel('Out')

    plt.show()



if __name__ == '__main__':

    filename = r'D:\Documents\open university\Seminar\datasets\calit2\CalIt2.data'
    in_df, out_df = load_calit2_data(filename)

    in_seq, in_period = create_time_sequence(in_df)
    out_seq, out_period = create_time_sequence(out_df)

    #print(out_period)
    plot(in_seq, out_seq, in_period)

