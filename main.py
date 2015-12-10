'''
Main of Program
=========================
Parameter Instruction.
sex    --> 0 == male and femal (default)
           1 == male only
           2 == female only

year_0 --> begin range of year. (default=1900)
year_1 --> end range of year.   (default=2011)

age_0  --> begin range of age.  (default=0)
age_1  --> end range of age.    (default=119)

'''
from data_tool import *
from matplotlib.dates import YearLocator, DateFormatter
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

def calculate_meandeath_men(num):
    """return a average death of men"""
    date = load_data(1)
    mean = sum(date[num])/120
    return mean

def calculate_meandeath_female(num):
    """return a average death of female"""
    date = load_data(2)
    mean = sum(date[num])/120
    return mean

def death_probability_graph_of_male_and_female():
    """Create death probability graph of male and female, black line represent as male and pink line represent as female"""

    date_lis = []
    mean_lis_men = []
    mean_lis_fem = []
    for i in range(1900, 2012):
        dates = dt.datetime(i, 1, 1)
        values_m = calculate_meandeath_men(i)
        values_f = calculate_meandeath_female(i)
        mean_lis_men.append(values_m*100)
        mean_lis_fem.append(values_f*100)
        date_lis.append(dates)

    fig, ax = plt.subplots()
    ax.plot_date(date_lis, mean_lis_men, 'b-', label = 'MALE', alpha=3, linewidth=2)
    ax.plot_date(date_lis, mean_lis_fem, '-', color='#ff3366', label = 'FEMALE', alpha=2, linewidth=2)
    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Year')
    plt.ylabel('Death Probability (%)')
    plt.title('Overall of death percent in each years')

    # format the ticks
    yearsFmt = DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

def overall_death_probability_graph(year_0=1900, year_1=2011):
    """Create Overall death probability graph, male female average,
       black represent as male,
       pink represent as female,
       blue represent as average.
    """
    # prepare data.---------------------------------------#
    dates, mean_m, mean_f, avg = [], [], [], []
    data_m = load_data(1)
    data_f = load_data(2)

    # process data.---------------------------------------#
    for year in range(year_0, year_1 + 1):
        date = dt.datetime(year, 1, 1)
        values_m = sum(data_m[year]) / len(data_m[year]) * 100
        values_f = sum(data_f[year]) / len(data_f[year]) * 100
        mean = (values_m + values_f) / 2

        dates.append(date)
        mean_m.append(values_m)
        mean_f.append(values_f)
        avg.append(mean)

    # plot graph.-----------------------------------------#
    fig, ax = plt.subplots()


    ax.plot_date(dates, mean_m, 'b-', label='Male', alpha=0.9, linewidth=2)
    ax.plot_date(dates, mean_f, '-', color='#ff3366', label='Female', alpha=0.9, linewidth=2)
    ax.plot_date(dates, avg, 'k-', label='avg.', alpha=1)

    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Year')
    plt.ylabel('Death Probability (%)')
    plt.title('Overall of death percent in each years')

    # format the ticks
    yearsFmt = DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)
    #show every year
    # years = YearLocator()
    # ax.xaxis.set_major_locator(years)

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

#overall_death_probability_graph()
death_probability_graph_of_male_and_female()
