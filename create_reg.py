import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, RegressorMixin, TransformerMixin
from sklearn.pipeline import make_pipeline

class Feature:
    def __init__(self, name, distribution, min_avg, max_var, coeff):
        self.name = name
        self.distribution = distribution
        self.min_avg = min_avg
        self.max_var = max_var
        self.coeff = coeff
        self.values= []

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

    if x1.distribution == "Normal Distribution":
        x1.values = np.random.normal(x1.min_avg, x1.max_avg, 10000)
    elif x1.distribution == "Uniform Distribution":
        x1.values = np.random.uniform(x1.min_avg, x1.max_avg, 10000)

    if x2.distribution == "Normal Distribution":
        x2.values = np.random.normal(x2.min_avg, x2.max_avg, 10000)
    elif x2.distribution == "Uniform Distribution":
        x2.values = np.random.uniform(x2.min_avg, x2.max_avg, 10000)
    
    if x3.distribution == "Normal Distribution":
        x3.values = np.random.normal(x3.min_avg, x3.max_avg, 10000)
    elif x3.distribution == "Uniform Distribution":
        x3.values = np.random.uniform(x3.min_avg, x3.max_avg, 10000)

    if x4.distribution == "Normal Distribution":
        x4.values = np.random.normal(x4.min_avg, x4.max_avg, 10000)
    elif x4.distribution == "Uniform Distribution":
        x4.values = np.random.uniform(x4.min_avg, x4.max_avg, 10000)

    if x5.distribution == "Normal Distribution":
        x5.values = np.random.normal(x5.min_avg, x5.max_avg, 10000)
    elif x5.distribution == "Uniform Distribution":
        x5.values = np.random.uniform(x5.min_avg, x5.max_avg, 10000)
    
    if x6.distribution == "Normal Distribution":
        x6.values = np.random.normal(x6.min_avg, x6.max_avg, 10000)
    elif x6.distribution == "Uniform Distribution":
        x6.values = np.random.uniform(x6.min_avg, x6.max_avg, 10000)

    y = x1.coeff * x1.values + x2.coeff * x2.values + x3.coeff * x3.values + x4.coeff * x4.values + x5.coeff * x5.values + x6.coeff * x6.values

    X = np.column_stack((x1.values, x2.values, x3.values, x4.values, x5.values, x6.values))



    return x1.values, x2.values, x3.values, x4.values, x5.values, x6.values, y



    