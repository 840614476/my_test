import matplotlib.pylab as pyl
import numpy as np

#正态分布直方图
data = np.random.normal(10.0, 1.0, 10000)
#生成直方图
pyl.hist(data)
pyl.show()
