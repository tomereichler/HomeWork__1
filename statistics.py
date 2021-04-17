import pandas


def statistics(pathToCSVFile):



def sum(values):
    sum=0
    for values in values:
        sum+=values
    return sum

def mean(values):
    count= len(values)
    sum1 = sum(values)
    return sum1/count


def median(values):
    val_list = list(values)
    val_list.sort()
    count = len(values)/2
    if count%2==0:
        return (val_list[count]+val_list[count+1])/2
    else:
        return val_list[count]

def population_statistics(feature_description, data, treatment, target, threshold, is_above, statistic_functions):
    pop_data= pandas.DataFrame(data,index)

    if is_above:
        for i in range(data[treatment]):
            if data[treatment][i] > threshold :
                pop_data = pop_data.loc

    else:

# START POINT
statistics(r'C:\Users\tomer\Desktop\london.csv')
