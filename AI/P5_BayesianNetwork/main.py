import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator

heartDisease = pd.read_csv('./AI/P5_BayesianNetwork/heart.csv')
heartDisease = heartDisease.replace('?',np.nan)

print('Few examples from the dataset are given below')
print(heartDisease.head())

network=BayesianNetwork(
    [
        ('age','trestbps'),
        ('age','fbs'),
        ('sex','trestbps'),
        ('exang','trestbps'),
        ('trestbps','heartdisease'),
        ('fbs','heartdisease'),
        ('heartdisease','restecg'),
        ('heartdisease','thalach'),
        ('heartdisease','chol')
    ])

print('\n Learning CPD using Maximum likelihood estimators')
network.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

print(network.get_cpds('heartdisease'))
