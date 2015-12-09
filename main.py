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

def calculate_meandeath_men(num):
    """return a average death"""
    date = load_data(1)
    mean = sum(date[num])/120
    return mean

def calculate_meandeath_female(num):
    """return a average death"""
    date = load_data(2)
    mean = sum(date[num])/120
    return mean
def graph_overall():
    """ create graph """

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
    ax.plot_date(date_lis, mean_lis_men, 'k-', label = 'MALE' )
    ax.plot_date(date_lis, mean_lis_fem, '-', color = '#ff3366', label = 'FEMALE' )
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

def overall_male_and_female():
    data_m = load_data(1)
    data_f = load_data(2)

    dates = [dt.datetime(i, 1, 1) for i in range(1900, 2012)]

    mean_m = [sum(data_m[i])/len(data_m[i]) for i in range(1900, 2012)]
    mean_f = [sum(data_f[i])/len(data_f[i]) for i in range(1900, 2012)]
    means = [(mean_m[i] + mean_f[i]) / 2 for i in range(len(mean_m))]

    fig, ax = plt.subplots()
    ax.plot_date(dates, means, '-')

    # format the ticks
    years = YearLocator() #show every year
    yearsFmt = DateFormatter('%Y')
    # ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate() #label type
    plt.show()
graph_overall()
