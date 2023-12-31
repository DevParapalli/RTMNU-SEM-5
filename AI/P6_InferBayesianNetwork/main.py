import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('./AI/P6_InferBayesianNetwork/heart.csv')
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
    ]
    )

print('\n Learning CPD using Maximum likelihood estimators')
network.fit(heartDisease,estimator=MaximumLikelihoodEstimator)

print('\n Inferencing with Bayesian Network:')
HeartDisease_infer = VariableElimination(network)

print('\n 1. Probability of HeartDisease given Age=45')
q=HeartDisease_infer.query(variables=['heartdisease'], evidence={'age':45})
print(q)