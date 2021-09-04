import csv
import pandas as pd
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("student_marks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math Score"], show_hist = False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
print("mean of population:-",mean)
print("standard deviation of population:-",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

mean = statistics.mean(mean_list)    
standard_deviation = statistics.stdev(mean_list)
print("mean of sample:- ", mean)
print("standard deviation of sample:- ",standard_deviation)

first_std_deviation_start, first_std_deviation_end = mean - standard_deviation, mean + standard_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*standard_deviation), mean + (2*standard_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*standard_deviation), mean + (3*standard_deviation)
"""print("std1:- ", first_std_deviation_start + first_std_deviation_end)
print("std2:- ", second_std_deviation_start + second_std_deviation_end)
print("std3:- ", third_std_deviation_start + third_std_deviation_end)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y=[0, 0.2], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
"""

df = pd.read_csv("School_1_Sample.csv")
data = df["Math_score"].tolist()

mean_of_sample_1 = statistics.mean(data)
print("mean of sample 1:- ", mean_of_sample_1)

fig = ff.create_distplot([mean_list], ["Student Marks"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean,mean], y = [0,0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()
