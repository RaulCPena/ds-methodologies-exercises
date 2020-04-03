# Create a py file that uses functions for exploring variables e.g (features & target)

# import all the needed modules for py file
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import warnings
warnings.filterwarnings("ignore")

import env
import wrangle
import split_scale

# write a function plot_variable_pairs(dataframe)
    # This function will plot all the pairwise relationships along with the regression line for each pair

def plot_variable_pairs(dataframe):
    """
    Args:
        dataframe (TYPE): df

    Returns:
        TYPE:Plots all of the pairwise relationships along with the regression line for eah pair
    """
    grades = sns.PairGrid(dataframe)
    grades.map(sns.regplot)
    plt.show()

# write a function calld months_to_years(tenure_months, df) which returns selected dataframe with a new feature tenure_years in complete years as a customer

def
