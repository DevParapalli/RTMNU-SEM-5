import numpy as np
import pandas as pd
from pgmpy.models import BayesianNetwork as BN
from pgmpy.estimators import MaximumLikelihoodEstimator as MLE
from pgmpy.inference import VariableElimination as VE

hd = pd.read_csv('./AI/P6_InferBayesianNetwork/heart.csv')
hd = hd.replace('?',np.nan)

print('Few examples from the dataset are given below')
print(hd.head())

nw=BN(
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
nw.fit(hd,estimator=MLE)

print('\n Inferencing with Bayesian Network:')
HeartDisease_infer = VE(nw)

print('\n 1. Probability of HeartDisease given Age=45')
q=HeartDisease_infer.query(variables=['heartdisease'], evidence={'age':45})
print(q)