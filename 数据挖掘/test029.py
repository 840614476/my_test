#读取博客数据并可视化

import pandas as pd
import matplotlib.pyplot as plt


#读入数据
data = pd.read_excel("F:/pycharm 文件/爬取网站/hexun.xls")
shape = data.shape
print(shape)

Data = data.T
#阅读数
y = Data.values[3]  #[第几行][第几列]
#评论数
x = Data.values[4]

plt.scatter(x,y)
plt.title("和讯博客阅读数和评论数")
plt.xlabel("评论数")
plt.ylabel("阅读数")
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()