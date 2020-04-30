"""
StockBrain 0.0.0 (also called as telencephalon)
"""
from Reader import StockReader

ot_source = StockReader('yahoo', 'RDS-A', '01-03-2000', '01-04-2020')
df_source = ot_source.read_stock()

