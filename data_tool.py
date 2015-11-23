'''specific tool fuction for our data processing.'''

def load_data(sex):
    '''return specific sex data_set in dict form.
       eg. {year: [rate of death]}
    '''
    import csv

    file = open('data/DeathProbsE_' + 'MF'[sex - 1] + '_Hist_TR2015.csv')
    data = csv.reader(file)
    data_set = [((int(row[0])), list(map(float, row[1:]))) for row in data if row[0].isnumeric()]

    return dict(data_set)

def select_data(year_0=1900, year_1=2011, age_0=0, age_1=119, sex=0):
    '''return data follow by range of years and ages.
       eg. male and female     --> {'m': {year: [rate of death]},
                                    'f': {year: [rate of death]}}

           male or female only --> {year: [rate of death]}
    '''
    data_set = dict()

    if sex == 0:
        data_set['m'] = select_data(year_0, year_1, age_0, age_1, 1)
        data_set['f'] = select_data(year_0, year_1, age_0, age_1, 2)
    elif sex == 1 or sex == 2:
        data = load_data(sex)
        for year in range(year_0, year_1 + 1):
            data_set[year] = data[year][age_0:age_1+1]

    return data_set
