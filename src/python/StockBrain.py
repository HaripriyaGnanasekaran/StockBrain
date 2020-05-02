"""
StockBrain 0.0.0 (also called as telencephalon)
"""
import pandas as md_pd
from Reader import Read 

# read stock 

cs_read = Read('stock')
df_source = cs_read.read_stock('yahoo', 'RDS-A', '01-03-2000', '01-04-2020')
print(df_source.head())

# stock read successfully!