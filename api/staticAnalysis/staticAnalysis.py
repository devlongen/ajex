import pandas as pd
import json
csv = pd.read_csv("/home/iagolongen/Downloads/student_habits_performance.csv")
class staticAnalysis:
    def __init__(self,df):
        self.df = pd.DataFrame(df) # get df the front
        self.lengthrow_dataframe,self.lengthcol_dataframe=self.df.shape # use pandas.shape(module)
        

    def lenghtDataframe(self) -> json:
        length_xandy = {"length_row":self.lengthrow_dataframe,"length_col":self.lengthcol_dataframe}
        json_response=json.dumps(length_xandy)
        return json_response
    
    def mean_dataframe(self) -> json:
        try:
            mean=self.df.mean(numeric_only=True,skipna=True)
            dict_mean = mean.to_dict()
            json_response=json.dumps(dict_mean)
            return json_response
        except:
            message="Error in the code not support for the mean dataframe"
            json_response=json.dumps(message)
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
        try:
            median=self.df.median(numeric_only=True,skipna=True)
            dict_median = median.to_dict()
            json_response=json.dumps(dict_median)
            return json_response
        except:
            message="Error in the code not support for the median dataframe"
            json_response=json.dumps(message)
            return json_response
        

    def cov_dataframe(self) -> json:
        return None
    def cor_dataframe(self) -> json:
        return None
        
        
app = staticAnalysis(csv)

test = app.median_dataframe()
print(test)