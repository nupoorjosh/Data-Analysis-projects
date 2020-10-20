#
#
#
#

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model, metrics
from Regression import Regression
class MainClass :
    def DataAnalysis(self):
        # Reading the data file into a pandas data frame
        lifedata = pd.read_csv("life_expectancy_dataset.csv")
        print("Data",lifedata)
        desc_data = lifedata.describe()
        # Obtaining a descriptive statistics of data
        print("Descriptive statistics of data:",desc_data)
        # Obtaining the total number of null values within the dataset
        nullvalues = lifedata.isnull().sum()
        print("Total null and missing values :",nullvalues)
        #Dropping the null values
        final_lifedata = lifedata.dropna(axis = 0,how = 'any')
        # Dropping columns having high multi-collinearity
        print("--------Cleaned data ----------")
        print(final_lifedata)
        # Creating instance of the class Regression
        reg = Regression()
        # Carrying out linear regression
        print("---------Visualisation  of data---------------")
        reg.visualisation(final_lifedata)
        reg_coef = []
        print("---------Multiple Regression of data---------------")
        reg_coef = reg.linearReg(final_lifedata)
        testdata = pd.read_csv("test.csv")
        print(testdata)
        replacements = {
         'Developing': 1,
         'Developed' : 0,
        }
        testdata['Status'].replace(replacements, inplace=True)
        ypred = []
        y_pred = 0
        for index, row in testdata.iterrows():
            y_pred = reg_coef[18] + reg_coef[0]* row['Year']+ reg_coef[1]* row['Status'] + reg_coef[2]* row['Adult Mortality']+ reg_coef[3]* row['infant deaths']+reg_coef[4]* row['Alcohol']
            reg_coef[5]* row['percentage expenditure'] + reg_coef[6]* row['Hepatitis B'] + reg_coef[7]* row['Measles '] + reg_coef[8]* row[' BMI '] + reg_coef[9]* row['Polio']
            reg_coef[10]* row['Total expenditure'] + reg_coef[11]* row['Diphtheria '] + reg_coef[12]* row[' HIV/AIDS'] + reg_coef[13]* row['GDP'] + reg_coef[14]* row['Population']
            + reg_coef[15]* row['thinness 5-9 years'] + reg_coef[16]* row['Income composition of resources'] + reg_coef[17]* row['Schooling'];
            ypred.append(y_pred)
        print("Predictions:")
        for i in ypred :
            print (i)
        # Carrying out logistic regression
        reg_coef = reg.logisticreg(final_lifedata)
# Creating instance of the main class
mainclass = MainClass()
mainclass.DataAnalysis()
