from matplotlib import pyplot

x = list(range(1,11))

y = [i**2 for i in x]

pyplot.plot(x, y, marker='o')

pyplot.title("Line Chart")
pyplot.xlabel("Number")
pyplot.ylabel("Square of Number")

pyplot.xticks(x)

pyplot.show()
