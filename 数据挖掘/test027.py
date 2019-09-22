import matplotlib.pylab as pyl
import numpy as np

data = np.random.randint(0, 25, 100)#（最小值，最大值，个数）
sty = np.arange(1, 30, 2)#（起始点，最终点，组距）
pyl.hist(data, sty)
pyl.show()