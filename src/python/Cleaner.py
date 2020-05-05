"""
Cleaner will clean the source data
"""
class Preprocessor:
    """
    Preprocess all the read data.
    """

    def __init__(self,df_source):
        self.df_source = df_source

    def choose(self,st_feature):
        df_data = self.df_source[st_feature]
        return df_data
