## Machine Learning Online Class - Exercise 3 | Part 2: Neural Networks

#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions 
#  in this exericse:
#
#     lrCostFunction.m (logistic regression cost function)
#     oneVsAll.m
#     predictOneVsAll.m
#     predict.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mention  d above.
#

## Initialization
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as io
import ex2helper as helper2
import ex3helper as helper

## Setup the parameters you will use for this exercise
input_layer_size  = 400;  # 20x20 Input Images of Digits
hidden_layer_size = 25;   # 25 hidden units
num_labels = 10;          # 10 labels, from 1 to 10   
                          # (note that we have mapped "0" to label 10)

## =========== Part 1: Loading and Visualizing Data =============
#  We start the exercise by first loading and visualizing the dataset. 
#  You will be working with a dataset that contains handwritten digits.
#

# Load Training Data
print('Loading and Visualizing Data ...')

mat = io.loadmat('./data/ex3data1.mat')
X = mat['X']
y = np.squeeze(mat['y'])


m = y.shape[0]

# Randomly select 100 data points to display
perm = np.random.permutation(m)
sel = X[perm[0:100],:]

#display data as image
helper.displayData(sel)


input('\nPart 1 completed. Program paused. Press enter to continue: ')


## ================ Part 2: Loading Pameters ================
# In this part of the exercise, we load some pre-initialized 
# neural network parameters.

print('Loading Saved Neural Network Parameters ...')

# Load the weights into variables Theta1 and Theta2
mat = io.loadmat('./data/ex3weights.mat')
theta1 = mat['Theta1']
theta2 = mat['Theta2']

## ================= Part 3: Implement Predict =================
#  After training the neural network, we would like to use it to predict
#  the labels. You will now implement the "predict" function to use the
#  neural network to predict the labels of the training set. This lets
#  you compute the training set accuracy.

