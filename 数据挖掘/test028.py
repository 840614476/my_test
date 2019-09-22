import matplotlib.pylab as pyl
import numpy as np

#子图

#第一个图
pyl.subplot(2,2,1)   #(行，列，当前区域)
x = [1,2,3,4,5]
y = [1,2,3,4,5]
pyl.plot(x,y)

#第二个图
pyl.subplot(2,2,2)

#第三个图
pyl.subplot(2,1,2)

pyl.show()