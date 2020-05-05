"""
StockBrain 0.0.0 (also called as telencephalon)
"""
import pandas as md_pd
from Reader import Read 
from Cleaner import Preprocessor

# read stock 

cs_read = Read('stock')
df_source = cs_read.read_stock('yahoo', 'RDS-A', '01-03-2000', '01-04-2020')

# choose the column needed to be analyzed.
cs_process = Preprocessor(df_source)
df_data = cs_process.choose('Close')
print(df_data.head(2))