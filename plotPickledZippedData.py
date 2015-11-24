import matplotlib
import cPickle as pickle

data = pickle.load(open( "/Users/Larry/Code/communication/pickledData.p", "rb" ))
plottableData = zip(*data)

scatter = matplotlib.pyplot.scatter(plottableData[0],plottableData[1])

matplotlib.pyplot.show()
