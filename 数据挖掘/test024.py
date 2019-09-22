import numpy as np

#随机数的生成
for i in range(0, 4):
    data = np.random.randint(1, 49, 6)  #(最小值，最大值，个数)
    print(data)