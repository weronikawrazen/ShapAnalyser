import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.base import BaseEstimator, RegressorMixin, TransformerMixin
from sklearn.pipeline import make_pipeline



class Feature:
    def __init__(self, name, distribution, min_avg, max_std, coeff):
        self.name = name
        self.distribution = distribution
        self.min_avg = min_avg
        self.max_std = max_std
        self.coeff = coeff
        self.values= None
        self.mean = 1
        self.std = 1
        self.min= 1
        self.q1= 1
        self.q2= 1
        self.q3= 1
        self.max= 1
        self.N = 10000

class MyOwnTransformer(BaseEstimator, TransformerMixin):
  def fit(self, X, y=None, alfa = None):
    return self
  def transform(self, X):
     return X

class MyOwnRegressor(BaseEstimator, RegressorMixin):
  def fit(self, X, y, alfa):
    return self
  def predict(self, X, alfa):
    #print(X.shape)
    Z = alfa[0] * X[:,0] + alfa[1] * X[:,1] + alfa[2] * X[:,2] + alfa[3] * X[:,3] + alfa[4] * X[:,4] + alfa[5] * X[:,5]
    return Z


def generate_data(x1,x2,x3,x4,x5,x6, r_seed_DGP):
    np.random.seed(r_seed_DGP)

    if x1.distribution == "Norm_dist":
        x1.values = np.random.normal(x1.min_avg, x1.max_std, 10000)
    elif x1.distribution == "Uni_dist":
        x1.values = np.random.uniform(x1.min_avg, x1.max_std, 10000)

    if x2.distribution == "Norm_dist":
        x2.values = np.random.normal(x2.min_avg, x2.max_std, 10000)
    elif x2.distribution == "Uni_dist":
        x2.values = np.random.uniform(x2.min_avg, x2.max_std, 10000)
    
    if x3.distribution == "Norm_dist":
        x3.values = np.random.normal(x3.min_avg, x3.max_std, 10000)
    elif x3.distribution == "Uni_dist":
        x3.values = np.random.uniform(x3.min_avg, x3.max_std, 10000)

    if x4.distribution == "Norm_dist":
        x4.values = np.random.normal(x4.min_avg, x4.max_std, 10000)
    elif x4.distribution == "Uni_dist":
        x4.values = np.random.uniform(x4.min_avg, x4.max_std, 10000)

    if x5.distribution == "Norm_dist":
        x5.values = np.random.normal(x5.min_avg, x5.max_std, 10000)
    elif x5.distribution == "Uni_dist":
        x5.values = np.random.uniform(x5.min_avg, x5.max_std, 10000)
    
    if x6.distribution == "Norm_dist":
        x6.values = np.random.normal(x6.min_avg, x6.max_std, 10000)
    elif x6.distribution == "Uni_dist":
        x6.values = np.random.uniform(x6.min_avg, x6.max_std, 10000)

    y = Feature('y',"none",0,0,1)
    y.values = x1.coeff * x1.values + x2.coeff * x2.values + x3.coeff * x3.values + x4.coeff * x4.values + x5.coeff * x5.values + x6.coeff * x6.values


    X = np.column_stack((x1.values, x2.values, x3.values, x4.values, x5.values, x6.values))
    
    for i in [x1, x2, x3, x4, x5, x6,y]:
        i.mean = np.mean(i.values)
        i.std = np.std(i.values)
        i.min= np.min(i.values)
        i.q1= np.quantile(i.values, .25)
        i.q2= np.quantile(i.values, .5)
        i.q3= np.quantile(i.values, .75)
        i.max= np.max(i.values)
        plt.subplots(figsize=(2.5, 4))
        plt.boxplot(i.values)
        plt.savefig(f'./static/images/dist_{i.name}.png')

    return x1, x2, x3, x4, x5, x6, y



    