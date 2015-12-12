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
import numpy as np
from matplotlib.dates import YearLocator, DateFormatter
from matplotlib.ticker import FormatStrFormatter
import datetime as dt
import matplotlib.pyplot as plt

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
        date = dt.datetime(year, 12, 31)
        values_m = sum(data_m[year]) / len(data_m[year]) * 100
        values_f = sum(data_f[year]) / len(data_f[year]) * 100
        mean = (values_m + values_f) / 2

        dates.append(date)
        mean_m.append(values_m)
        mean_f.append(values_f)
        avg.append(mean)

    # plot graph.-----------------------------------------#
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.plot_date(dates, mean_m, 'b-', label='Male', alpha=0.9, linewidth=2)
    ax.plot_date(dates, mean_f, 'r-', label='Female', alpha=0.9, linewidth=2)
    ax.plot_date(dates, avg, 'k-', label='avg.', alpha=1)

    # format the ticks.-----------------------------------#
    years = YearLocator(5, 12, 31) # every year, month, day
    yearsFmt = DateFormatter('%Y')
    yticks = FormatStrFormatter('%.0f%%')
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.yaxis.set_major_formatter(yticks)
    ax.autoscale_view()
    ax.grid(True)

    # expression.-----------------------------------------#
    plt.rcParams.update({'font.size': 17})
    plt.xlabel('Years')
    plt.ylabel('Death Probability')
    plt.title('Overall of death percent in each years.')

    fig.autofmt_xdate()
    plt.legend()
    plt.show()

def death_probability_graph_in_bar_graph():
    """
    Create Death probability of each generation in bar graph, a graph points
    about death probability in each age.
    0 - 3 baby
    4 - 6 early childhood
    7 - 12 middle childhood
    13 -20 teenager
    21 - 40 early adulthood
    41 - 60 middle adulthood
    61 - 119 old age
    """
    data_m = load_data(1)
    data_f = load_data(2)
    age = ('Baby', 'Early Childhood', 'Middle Childhood', 'Teenager',
           'Early Adulthood', 'Middle Adulthood', 'Old')

    index = np.arange(len(age))
    bar_width = 0.35
    x = index
    y_m = [0] * len(age)
    y_f = [0] * len(age)

    for year in range(1900, 2012):
        y_m[0] += sum(data_m[year][0:4])/len(data_m[year][0:4])
        y_m[1] += sum(data_m[year][4:7])/len(data_m[year][4:7])
        y_m[2] += sum(data_m[year][7:13])/len(data_m[year][7:13])
        y_m[3] += sum(data_m[year][13:21])/len(data_m[year][13:21])
        y_m[4] += sum(data_m[year][21:41])/len(data_m[year][21:41])
        y_m[5] += sum(data_m[year][41:61])/len(data_m[year][41:61])
        y_m[6] += sum(data_m[year][61:])/len(data_m[year][61:])
        #y_m[7] += sum(data_m[year][81:])/len(data_m[year][81:])

        y_f[0] += sum(data_f[year][0:4])/len(data_f[year][0:4])
        y_f[1] += sum(data_f[year][4:7])/len(data_f[year][4:7])
        y_f[2] += sum(data_f[year][7:13])/len(data_f[year][7:13])
        y_f[3] += sum(data_f[year][13:21])/len(data_f[year][13:21])
        y_f[4] += sum(data_f[year][21:41])/len(data_f[year][21:41])
        y_f[5] += sum(data_f[year][41:61])/len(data_f[year][41:61])
        y_f[6] += sum(data_f[year][61:])/len(data_f[year][61:])
        #y_f[7] += sum(data_f[year][81:])/len(data_f[year][81:])

    for i in range(7):
        y_m[i] = y_m[i] / 112 * 100
        y_f[i] = y_f[i] / 112 * 100

    fig,(ax,ax2) = plt.subplots(1, 2, sharey=True)

    ax.barh(x, y_m, bar_width, color='b', label='Male')
    ax.barh(x + bar_width, y_f, bar_width, color='r', label='Female')
    ax2.barh(x, y_m, bar_width, color='b', label='Male')
    ax2.barh(x + bar_width, y_f, bar_width, color='r', label='Female')

    ax.set_xlim(0, 6)
    ax2.set_xlim(25, 35)
    ax.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    ax.yaxis.tick_left()
    ax.tick_params(labeltop='off') # don't put tick labels at the top
    ax2.yaxis.tick_right()

    plt.subplots_adjust(wspace=0.075)
    d = .015 # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    ax.plot((1-d,1+d),(-d,+d), **kwargs) # top-left diagonal
    ax.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal

    kwargs.update(transform=ax2.transAxes) # switch to the bottom axes
    ax2.plot((-d,d),(-d,+d), **kwargs) # top-right diagonal
    ax2.plot((-d,d),(1-d,1+d), **kwargs) # bottom-right diagonal

    plt.setp(ax2.get_yticklabels(), visible=False)
    plt.yticks(x + bar_width, age)
    ax.set_ylabel('Age')
    plt.legend(loc=4)
    fig.text(0.5, 0.04, 'Death Chance', ha='center')

    fig.suptitle("Death Probability of each Generation.", fontsize=14, fontweight='bold')
    plt.show()

death_probability_graph_in_bar_graph()
