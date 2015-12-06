'''sample graph by pyplot.'''
import numpy as np
import matplotlib.pyplot as plt

def bar_vertical():
    age = ('Child', 'Teen', 'Adult', 'Old', 'Immortal')

    index = np.arange(len(age))
    bar_width = 0.35

    x = index                         #ตำแหน่งของ bar
    y_m = [50, 25, 75, 100, 0]        #ค่าของแต่ละ bar
    y_f = [75, 50, 80, 120, 10]       #ค่าของแต่ละ bar

    plt.bar(x, y_m, bar_width, color='b', label='Male')                 #วาดกราฟ1
    plt.bar(x + bar_width, y_f, bar_width, color='r', label='Female')   #วาดกราฟ2

    plt.xticks(x + bar_width, age)    #ชื่อ bar เรียงตามตำแหน่ง
    plt.xlabel('Age Group')           #ชื่อ แกน x
    plt.ylabel('Death Chance (%)')    #ชื่อ แกน y
    plt.title('Title Here')           #ชื่อ กราฟ
    plt.legend()                      #แสดง label ของ bar

    plt.show()                        #แสดงกราฟ

def bar_horizon():
    age = ('Child', 'Teen', 'Adult', 'Old', 'Immortal')

    index = np.arange(len(age))
    bar_width = 0.35

    x = index
    y_m = [50, 25, 75, 100, 0]
    y_f = [75, 50, 80, 120, 10]

    plt.barh(x, y_m, bar_width, color='b', label='Male')
    plt.barh(x + bar_width, y_f, bar_width, color='r', label='Female')

    plt.yticks(x + bar_width, age)
    plt.ylabel('Age')
    plt.xlabel('Death Chance (%)')
    plt.title('Title Here')
    plt.legend()

    plt.show()

def plot_date_graph():
    from matplotlib.dates import YearLocator, DateFormatter
    import datetime as dt

    dates = [dt.datetime(i, 1, 1) for i in range(1900, 1910)]
    values = [6, 12, 3, 7, 2, 20, 5, 11, 7, 15]

    fig, ax = plt.subplots()
    ax.plot_date(dates, values, '-')

    # format the ticks
    yearsFmt = DateFormatter('%Y')
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.autoscale_view()
    ax.grid(True)

    fig.autofmt_xdate()
    plt.show()
