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

def select_data(year_0=1900, year_1=2011, age_0=0, age_1=119):
    '''return data follow by range of years and ages.'''
