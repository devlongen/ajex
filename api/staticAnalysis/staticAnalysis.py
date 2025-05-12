import pandas as pd
import numpy as np
csv = pd.read_csv("/home/iagolongen/Downloads/student_habits_performance.csv")
class staticAnalysis:
    def __init__(self,df):
        self.df = pd.DataFrame(df) # get df the front
        self.lengthrow_dataframe,self.lengthcol_dataframe=self.df.shape # use pandas.shape(module)
        self.mean_dataframe_col=dict # create function mean and for col
        self.sum_dataframe_col=dict # create function sum and for col
        self.min_dataframe_col=dict # create function min and for col
        self.max_dataframe_col=dict # create function max and for col
        self.mfv_dataframe_col=dict # create function modeest
        self.median_dataframe_col=dict # create function
        self.cov_dataframe_col=dict # create function
        self.cor_dataframe_col=dict # create function

    def lenghtDataframe(self) -> dict:
        dict_length = {"length_row":self.lengthrow_dataframe,"length_col":self.lengthcol_dataframe}
        return dict_length
    
    def basic_statistics(self) -> dict:
        # variables
        qtd_row = self.lengthrow_dataframe
        qtd_column = self.lengthcol_dataframe

        
        # create function
        def mean_dataframe(qtd_row,qtd_column) -> dict:
            sum_value=0
            for i in range(qtd_row):
                value = self.df.iloc[i]
                if value is int:
                    sum_value = sum_value + value
                else:
                    pass
            mean_var = sum_value/qtd_row
            dict_mean = {"mean":mean_var}
            
            print(dict_mean)
            return dict_mean
        
        def sum_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def min_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def max_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def mfv_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def median_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def cov_dataframe(qtd_row,qtd_column) -> dict:
            return None
        def cor_dataframe(qtd_row,qtd_column) -> dict:
            return None
        
        # function
        mean_dataframe(qtd_row,qtd_column)
        sum_dataframe(qtd_row,qtd_column)
        min_dataframe(qtd_row,qtd_column)
        max_dataframe(qtd_row,qtd_column)
        mfv_dataframe(qtd_row,qtd_column)
        median_dataframe(qtd_row,qtd_column)
        cov_dataframe(qtd_row,qtd_column)
        cor_dataframe(qtd_row,qtd_column)


app = staticAnalysis(csv)

test = app.basic_statistics()