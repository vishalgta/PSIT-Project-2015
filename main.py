'''
Main of Program
'''
from data_tool import *
import numpy as np
from matplotlib.dates import YearLocator, DateFormatter
from matplotlib.ticker import FormatStrFormatter
import datetime as dt
import matplotlib.pyplot as plt

def overall_death_probability_graph(year_0=1900, year_1=2011):
    """Create Overall death probability graph male and female
       black represent as male,
       pink represent as female.
    """
    # prepare data.---------------------------------------#
    dates, mean_m, mean_f = [], [], []
    data_m = load_data(1)
    data_f = load_data(2)

    # process data.---------------------------------------#
    for year in range(year_0, year_1 + 1):
        date = dt.datetime(year, 12, 31)
        values_m = sum(data_m[year]) / len(data_m[year]) * 100
        values_f = sum(data_f[year]) / len(data_f[year]) * 100

        dates.append(date)
        mean_m.append(values_m)
        mean_f.append(values_f)

    # plot graph.-----------------------------------------#
    fig, ax = plt.subplots(figsize=(18, 6))

    ax.plot_date(dates, mean_m, 'b-', label='Male', alpha=0.9, linewidth=2)
    ax.plot_date(dates, mean_f, 'r-', label='Female', alpha=0.9, linewidth=2)

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

def calculate_mean_of_each_generation(num, k, mem):
    """return mean of each generation"""
    if k <= 3:
        mem.append(num)
        if len(mem) == 4:
            return sum(mem)/4
    elif k <= 6:
        mem.append(num)
        if len(mem) == 3:
            return sum(mem)/3
    elif k <= 12:
        mem.append(num)
        if len(mem) == 6:
            return sum(mem)/6
    elif k <= 19:
        mem.append(num)
        if len(mem) == 7:
            return sum(mem)/7
    elif k <= 39:
        mem.append(num)
        if len(mem) == 20:
            return sum(mem)/20
    elif k <= 59:
        mem.append(num)
        if len(mem) == 20:
            return sum(mem)/20
    elif k <= 119:
        mem.append(num)
        if len(mem) == 60:
            return sum(mem)/60

def death_probability_graph_in_bar_graph():
    """
    Create Death probability of each generation in bar graph, a graph points
    about death probability in each age.
    0 - 3 baby
    4 - 6 early childhood
    7 - 12 middle childhood
    13 -19 teenager
    21 - 39 early adulthood
    41 - 59 middle adulthood
    61 - 119 old age
    """
    # prepare data.---------------------------------------#
    age = ('Baby', 'Early Childhood', 'Middle Childhood', 'Teenager',
           'Early Adulthood', 'Middle Adulthood', 'Old')
    men_data = load_data(1)
    female_data = load_data(2)
    lis_men = []
    lis_fm = []
    baby_list = []
    early_child_list = []
    middle_child_list = []
    teenager_list = []
    early_adult_list = []
    middle_adult_list = []
    old_age_list = []
    baby_list_fm = []
    early_child_list_fm = []
    middle_child_list_fm = []
    teenager_list_fm = []
    early_adult_list_fm = []
    middle_adult_list_fm = []
    old_age_list_fm = []
    sex_men = []
    sex_fm = []
    mem = []

    # process data.---------------------------------------#
    for i in range(1900, 2012):
        lis_men = []
        lis_fm = []
        lis_men.append(men_data[i])
        lis_fm.append(female_data[i])
        for k in range(len(lis_men[0])):
            if k <= 3:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    baby_list.append(values)
                    mem = []
            elif k <= 6:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    early_child_list.append(values)
                    mem = []
            elif k <= 12:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    middle_child_list.append(values)
                    mem = []
            elif k <= 19:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    teenager_list.append(values)
                    mem = []
            elif k <= 39:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    early_adult_list.append(values)
                    mem = []
            elif k <= 59:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    middle_adult_list.append(values)
                    mem = []
            elif k <= 119:
                values = calculate_mean_of_each_generation(lis_men[0][k], k, mem)
                if values != None:
                    old_age_list.append(values)
                    mem = []
        for j in range(len(lis_fm[0])):
            if j <= 3:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    baby_list_fm.append(values)
                    mem = []
            elif j <= 6:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    early_child_list_fm.append(values)
                    mem = []
            elif j <= 12:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    middle_child_list_fm.append(values)
                    mem = []
            elif j <= 19:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    teenager_list_fm.append(values)
                    mem = []
            elif j <= 39:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    early_adult_list_fm.append(values)
                    mem = []
            elif j <= 59:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    middle_adult_list_fm.append(values)
                    mem = []
            elif j <= 119:
                values = calculate_mean_of_each_generation(lis_fm[0][j], j, mem)
                if values != None:
                    old_age_list_fm.append(values)
                    mem = []

    sex_men.append((sum(baby_list)/112)*100)
    sex_men.append((sum(early_child_list)/112)*100)
    sex_men.append((sum(middle_child_list)/112)*100)
    sex_men.append((sum(teenager_list)/112)*100)
    sex_men.append((sum(early_adult_list)/112)*100)
    sex_men.append((sum(middle_adult_list)/112)*100)
    sex_men.append((sum(old_age_list)/112)*100)
    sex_fm.append((sum(baby_list_fm)/112)*100)
    sex_fm.append((sum(early_child_list_fm)/112)*100)
    sex_fm.append((sum(middle_child_list_fm)/112)*100)
    sex_fm.append((sum(teenager_list_fm)/112)*100)
    sex_fm.append((sum(early_adult_list_fm)/112)*100)
    sex_fm.append((sum(middle_adult_list_fm)/112)*100)
    sex_fm.append((sum(old_age_list_fm)/112)*100)

    # plot graph.-----------------------------------------#
    index = np.arange(len(age))
    bar_width = 0.35
    x = index

    fig,(ax,ax2) = plt.subplots(1, 2, sharey=True)

    ax.barh(x, sex_men, bar_width, color='b', label='Male')
    ax.barh(x + bar_width, sex_fm, bar_width, color='r', label='Female')
    ax2.barh(x, sex_men, bar_width, color='b', label='Male')
    ax2.barh(x + bar_width, sex_fm, bar_width, color='r', label='Female')

    ax.set_xlim(0, 6)
    ax2.set_xlim(27, 32)
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

def surface_overall_deadth_prob():
    """Create 3d Surface Graph overall deadth probability."""
    import plotly.plotly as py
    import plotly.tools as tls
    from plotly.graph_objs import *
    #py.sign_in("username", "api key")

    data_m = load_data(1)
    data_f = load_data(2)

    x = list(range(120))
    y = list(range(1900, 2012))
    z = []

    for year in range(1900, 2012):
        temp = []
        for age in range(120):
            temp.append((data_m[year][age] + data_f[year][age]) / 2)
        z.append(temp)

    trace = [Surface(z=z, x=x, y=y)]

    fig = Figure(data=trace)
    plot_url = py.plot(fig, filename="Overall Death Probability Surface Graph.")

# overall_death_probability_graph()
# death_probability_graph_in_bar_graph()
# surface_overall_deadth_prob()
