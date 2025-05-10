import pandas as pd

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
        dataframe_work = self.df
        n_row = self.lengthrow_dataframe
        n_column = self.lengthcol_dataframe
        
        # function
        mean_dataframe(dataframe_work,n_row,n_column)
        sum_dataframe(dataframe_work,n_row,n_column)
        min_dataframe(dataframe_work,n_row,n_column)
        max_dataframe(dataframe_work,n_row,n_column)
        mfv_dataframe(dataframe_work,n_row,n_column)
        median_dataframe(dataframe_work,n_row,n_column)
        cov_dataframe(dataframe_work,n_row,n_column)
        cor_dataframe(dataframe_work,n_row,n_column)

        # create function
        def mean_dataframe(param,number_row,number_column) -> dict:
            return None
        def sum_dataframe(param,number_row,number_column) -> dict:
            return None
        def min_dataframe(param,number_row,number_column) -> dict:
            return None
        def max_dataframe(param,number_row,number_column) -> dict:
            return None
        def mfv_dataframe(param,number_row,number_column) -> dict:
            return None
        def median_dataframe(param,number_row,number_column) -> dict:
            return None
        def cov_dataframe(param,number_row,number_column) -> dict:
            return None
        def cor_dataframe(param,number_row,number_column) -> dict:
            return None
        
