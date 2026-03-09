import pandas
from matplotlib import pyplot

titanic_data = pandas.read_csv('titanic.csv')

pclass_counts = titanic_data['Pclass'].value_counts().reindex([1,2,3])

pclass_counts.plot(kind='bar', color=['lightblue','lightgreen','salmon'])

pyplot.title('Bar Chart - Titanic Data Set')
pyplot.xlabel('Passenger Class')
pyplot.ylabel('Number of Passengers')

pyplot.xticks(rotation='horizontal')

pyplot.show()
