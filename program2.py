import pandas
from matplotlib import pyplot

titanic_data = pandas.read_csv('titanic.csv')

titanic_data['Fare'].plot(kind='hist', edgecolor="black", bins=30)

pyplot.title("Histogram - Titanic Data Set")
pyplot.xlabel('Fare')

pyplot.show()
