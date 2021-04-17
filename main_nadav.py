import os
from pandas import read_csv
import pandas



def main_nadav(pathToCSVFile):
    # Check that input path is exist
    if os.path.isfile(pathToCSVFile):
        # load the CSV file content using Pandas
        features = ['hum', 't1', 'cnt', 'season', 'is_holiday']
        data = load_data(pathToCSVFile, features)
        x = 5
        dt1 = {}
        dt2 = {}
        feature = 'hum'
        dt1, dt2 = filter_by_feature(data,feature, data[feature])
        y = 10


# ====================loading the data and return filtered data=====================
def load_data(pathToCSVFile, features):
    df = pandas.read_csv(pathToCSVFile)
    data = df.to_dict(orient="list")
    filtered_data = {features: data[features] for features in features}
    return filtered_data


# ==================================================#
def filter_by_feature(data, feature, values):
    data1 = data.copy()
    data2 = {}
    data2[feature] = values
    data1.pop(feature, values)
    return data1,data2

def print_details(data, features, statistic_functions)
    print()

# START POINT
main_nadav(r'C:\Users\tomer\Desktop\london.csv')
