import numpy
import pandas

titanic_data = pandas.read_csv('titanic.csv')

data_array = titanic_data.to_numpy()
number_of_passengers = data_array.shape[0]

number_of_survivors = numpy.sum(data_array[:,1])

ages = data_array[:,5]
ages = ages.astype(float)
average_age = numpy.nanmean(ages)

print("Number of passengers:", number_of_passengers)
print("Number of survivors:", number_of_survivors)
print("Average age of passengers:", "%.2f" % average_age)
