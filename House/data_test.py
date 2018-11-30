from pydoc import help
from scipy.stats.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
from pandas import DataFrame
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

#print(dataframe)
# #Git rid of the name of the animal
# #And change the hunter/scavenger to 0/1
# dataframe = dataframe.drop(["Name"], axis = 1)
# cleanup = {"Class": {"Primary Hunter" : 0, "Primary Scavenger": 1     }}
# dataframe.replace(cleanup, inplace = True)
# print(dataframe.head())
#array = dataframe.values
#print(array)
# #Data splt
# # Seperating the data into dependent and independent variables


# print(pearsonr(c, y)) //calculated carrecation

# print(X)
# print(y)
#
# #
# logReg = LinearRegression()
# logReg.fit(X,y)
# # logReg.fit(X,y)
# pred = logReg.predict([[2,0,42,11,1]])
# # #print('Variance score: %.2f' % r2_score([[43500]],pred))
# print(pred)
class Data(object):


    @staticmethod
    def data_min(ar):

        print("here")
        filename = 'House/my.csv'
        # Data set Preprocess data
        dataframe = pd.read_csv(filename)
        X = dataframe.iloc[:, 0:-1]
        y = dataframe.iloc[:, -1]
        logReg = LinearRegression()
        logReg.fit(X, y)
        # logReg.fit(X,y)
        pred = logReg.predict(ar)
        # #print('Variance score: %.2f' % r2_score([[43500]],pred))
        return pred
# print(logReg.coef_,"hh")

# #logReg.fit(dataframe.iloc[-1:],dataframe.iloc[:,-1])