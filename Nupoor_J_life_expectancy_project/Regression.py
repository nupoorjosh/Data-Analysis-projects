
#
#


import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn import datasets, linear_model, metrics

class Regression :
    def visualisation(self,data):
        print(data.info())
        # Status vs Life Expectancy
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        sns.boxplot(x='Status',y='Life expectancy ',
        data= data[['Status','Life expectancy ']])
        plt.show()
        # Life expectancy over the years 
        sns.lineplot('Year', 'Life expectancy ', data=data, marker='o')
        plt.title('Life Expectancy by Year')
        plt.show()
        # Adult_mortality vs Life Expectancy
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        sns.set(font_scale=2)
        sns.scatterplot(x="Adult Mortality", y="Life expectancy ",palette="rocket",data=data[['Adult Mortality','Life expectancy ']]);
        plt.show()
        # Life expectancy vs total expenditure
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        sns.set(font_scale=1)
        sns.regplot(x="Total expenditure", y="Life expectancy ", data=data[['Total expenditure','Life expectancy ']])
        ax.set_title('Life_expectancy vs Total expenditure')
        plt.show()
        # Life expectancy vs Alcohol consumption
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        x = data['Alcohol']
        plt.hist(x,bins=10)
        ax.set_title('Alcohol consumption frequency')
        plt.show()
        # Number of polio cases over the years
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        sns.set(font_scale=1)
        sns.barplot(x="Year", y="Polio",palette = 'deep', data=data[['Year','Polio']])
        ax.set_title('Year vs Polio')
        plt.show()
        plt.show()
        # Life expectancy over the years 
        sns.regplot(' HIV/AIDS', 'Life expectancy ', data=data, marker='o')
        plt.title('Life Expectancy by HIV/AIDS')
        plt.show()
        # Life expectancy vs Income composition of resources
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        sns.set(font_scale=1)
        sns.regplot(x="Income composition of resources", y="Life expectancy ", data=data[['Income composition of resources','Life expectancy ']])
        ax.set_title('Life_expectancy vs Income composition of resources')
        plt.show()
    def linearReg(self,data):
        print("Data to be worked on")
        print(data)
        reg_coefficients = list()
        life_exp_data = data.copy()
        life_exp_data['Status'] = life_exp_data['Status'].astype('category') # The column status is converted into numerical format by first converting it to category.
        life_exp_data['Status'] = life_exp_data['Status'].cat.codes
        print(life_exp_data['Status'])
        # Checking the correlation between the variables
        #Plotting heat maps along with the correlation values
        plt.figure(figsize=(120,40))
        cor = life_exp_data.corr()
        sns.heatmap(cor, annot=True,annot_kws={"size": 6},vmax=.5, square=True,cmap="RdYlGn")
        plt.show()
        # Defining X and Y for training and testing
        X = life_exp_data.drop(columns = ['Life expectancy ','Country','under-five deaths ',' thinness  10-19 years'])
        y = life_exp_data['Life expectancy ']
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=1/3)
        x_train.isnull().sum()
        y_train.isnull().sum()
        x_test.isnull().sum()
        y_test.isnull().sum()
        x_train.fillna(0)
        y_train.fillna(0)
        x_test.fillna(0)
        y_test.fillna(0)
        print("------Training test split--------------")
        print(x_train.shape)
        print(x_test.shape)
        print(y_train.shape)
        print(y_test.shape)
        print(x_train.dtypes)
        #x_train.to_excel("xtrain.xlsx", engine='xlsxwriter')
        # Using linear regression model to fit the data
        model_reg = linear_model.LinearRegression()
        # Fitting the model
        model_reg.fit(x_train,y_train)
        # Determine the R2 (Goodness of fit test score)
        print("Regression score :",model_reg.score(x_train,y_train))
        # Determining the regression co-efficients
        print("Regression co-efficients", model_reg.coef_)
        print("Regression intercept:",model_reg.intercept_)
        predictionvalues = model_reg.predict(x_test)
        predictionsdf = pd.DataFrame(predictionvalues)
        predictionsdf.to_excel("output_mlr.xlsx", engine='xlsxwriter')
        print("-----------Predictions done --------Predictions are printed to output file------------------")
        ## Plot of actual vs predicted values
        fig = plt.figure(figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.set_title('Actual values vs Predicted values')
        plt.scatter(y_test, predictionvalues)
        plt.xlabel('Actual_values')
        plt.ylabel('Predicted_values')
        plt.show()
        # Plotting residual plots in order to evaluate performance of the model
        predictionsdf.columns = ['Life expectancy']
        y_test_df = pd.DataFrame(y_test)
        y_test_df.columns = ['Life expectancy']
        print(y_test_df)
        final_df = pd.DataFrame({'Actual_values':y_test, 'Predicted_values':predictionvalues})
        print(final_df)
        true_val = y_test_df['Life expectancy'].values.copy()
        pred_val = predictionsdf['Life expectancy'].values.copy()
        residual = true_val - pred_val
        fig, ax = plt.subplots(figsize=(25,10))
        ax.set_title('Residuals vs Predicted values')
        plt.scatter(predictionvalues, residual)
        plt.xlabel('Predictated value for life expectancy')
        plt.ylabel('Residual')
        plt.show()
        _ = ax.scatter(pred_val,residual)
        # Evaluating the performance measures of the model
        from sklearn import metrics
        print("Evaluation of the prediction model : Mean Absolute error")
        print(metrics.mean_absolute_error(y_test,predictionsdf))
        print("Mean Squared error")
        print(metrics.mean_squared_error(y_test,predictionsdf))
        print("Root mean squared error")
        print(np.sqrt(metrics.mean_squared_error(y_test, predictionsdf)))
        for i in model_reg.coef_ :
            reg_coefficients.append(i)
        reg_coefficients.append(model_reg.intercept_)
        return reg_coefficients

    def logisticreg(self,life_exp_data):
        #Splitting train test for logistic regression
        print("--------Performing logistic regression----------")
        life_exp_data['Status'] = life_exp_data['Status'].astype('category') # The column status is converted into numerical format by first converting it to category.
        life_exp_data['Status'] = life_exp_data['Status'].cat.codes
        from sklearn.model_selection import train_test_split
        xtrain, xtest, ytrain, ytest = train_test_split(life_exp_data.drop(columns = ['Status','Country','under-five deaths ',' thinness  10-19 years']),
                                                        life_exp_data['Status'], test_size=0.30,random_state=0)
        # Building the logistic model
        from sklearn.linear_model import LogisticRegression
        logmodel = LogisticRegression()
        logmodel.fit(xtrain,ytrain)
        predictions = logmodel.predict(xtest)
        print("Predicted values of logistic regression :")
        print(predictions)
        predictionsdf = pd.DataFrame(predictions)
        predictionsdf.to_excel("output_logistic.xlsx", engine='xlsxwriter')
        print("-----------Predictions done --------Predictions are printed to output file------------------")
        final_df = pd.DataFrame({'Actual_values':ytest, 'Predicted_values':predictions})
        print(final_df)
        
        
        
        













