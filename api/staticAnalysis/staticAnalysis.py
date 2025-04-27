import pandas as pd

class staticAnalysis:
    def __init__(self,df):
        self.df = pd.DataFrame(df)  
    
    def insightDataframe(self):
        dfInsight=self.df
        return dfInsight