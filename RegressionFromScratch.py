#m = (mean of X* Mean of y - mean of Xy)/(mean of x)^2- mean of (x)^2

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([5,4,6,5,6,7], dtype = np.float64)

#plt.scatter(xs, ys)
#plt.show()
#PEMDAS
#mean(xs)^2, mean(xs)**
def best_fit_slope_and_intercept(xs, ys):
    m =( ((mean(xs) * mean(ys)) - mean(xs*ys))/
           ((mean(xs)*mean(xs))- mean(xs*xs)) )

    b = mean(ys) - m*mean(xs)
    return m, b

m,b = best_fit_slope_and_intercept(xs, ys)

#print(m,b)

regression_line = [(m*x)+b for x in xs]

predict_x = 25
predict_y = (m*predict_x)+b

plt.scatter(xs,ys)
plt.scatter(predict_x,predict_y, color='green')
plt.plot(xs, regression_line)
plt.show()
