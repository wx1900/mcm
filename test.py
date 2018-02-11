# -*- coding: utf-8 -*- 
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler    #引入缩放的包
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split # 分割数据模块
import csv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-4, 4, 0.25)
Y = np.arange(-8, 8, 0.5)
X, Y = np.meshgrid(X, Y)
Z = X + Y
# Z = np.sin(R)
print(X)
print(Y)
print(Z)
# 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

plt.show()