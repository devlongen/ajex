import pandas as pd
import json
csv = pd.read_csv("/home/iagolongen/Downloads/student_habits_performance.csv")
class staticAnalysis:
    def __init__(self,df):
        self.df = pd.DataFrame(df) # get df the front
        self.lengthrow_dataframe,self.lengthcol_dataframe=self.df.shape # use pandas.shape(module)
        self.mean_dataframe_col=json # create function mean and for col
        self.sum_dataframe_col=json # create function sum and for col
        self.min_dataframe_col=json # create function min and for col
        self.max_dataframe_col=json # create function max and for col
        self.mfv_dataframe_col=json # create function modeest
        self.median_dataframe_col=json # create function
        self.cov_dataframe_col=json # create function
        self.cor_dataframe_col=json # create function

    def lenghtDataframe(self) -> json:
        json_length = {"length_row":self.lengthrow_dataframe,"length_col":self.lengthcol_dataframe}
        return json_length
    
    def mean_dataframe(self) -> json:
        df_tratament = self.df
        mean=df_tratament.mean(numeric_only=True,skipna=True)
        json_response=json.dumps({"mean:":mean})
        return json_response
        
    def sum_dataframe(self) -> json:
        return None
    def min_dataframe(self) -> json:
        return None
    def max_dataframe(self) -> json:
        return None
    def mfv_dataframe(self) -> json:
        return None
    def median_dataframe(self) -> json:
        return None
    def cov_dataframe(self) -> json:
        return None
    def cor_dataframe(self) -> json:
        return None
        
        
app = staticAnalysis(csv)

test = app.mean_dataframe()