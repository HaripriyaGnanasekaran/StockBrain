import pandas_datareader.data as web
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import pandas as pd

pf_return = []
pf_risk = []
stocklist = ['GOOG', 'SPY', 'RDS-A', 'BABA',
             'AMZN', 'ENPH', 'TSLA', 'MSFT', 'MA', 'AAPL']


for runs in range(1, 2):

    weight = 1.0/len(stocklist)
    w4 = float(runs)/float(20.0)
    w = float(1.0-w4)/float(3)
    opt_weight = []
    avg_return = []
    avg_std = []
    for name in stocklist:
        df = web.get_data_yahoo(name, '01/01/2004', interval='m')
        close = df['Close']
        returns = close.pct_change()
        mu = returns.mean()
        sigma = returns.std()
        maxprice = mu+sigma
        minprice = mu-sigma
        opt_weight.append(weight)
        avg_return.append(mu)
        avg_std.append(sigma)

    dictionary = {'Stock': stocklist, 'weight': opt_weight,
                  'return': avg_return, 'std': avg_std}
    df = pd.DataFrame.from_dict(dictionary)

    wt_return = sum((df['return'])*df['weight'])

    # covariance matrix
    cov = {}
    df_cov = pd.DataFrame(columns=stocklist)
    for name in stocklist:
        df1 = web.get_data_yahoo(name, '01/01/2004', interval='m')
        df1[name] = df1['Close'].pct_change()
        row = []
        for stock in stocklist:
            df2 = web.get_data_yahoo(stock, '01/01/2004', interval='m')
            df2[stock] = df2['Close'].pct_change()
            row.append(df1[name].cov(df2[stock]))
        cov.update({name: row})

    df_cov = pd.DataFrame.from_dict(cov)
    df_cov['weight'] = opt_weight

    df_port_cov = df_cov[:]
    df_port_cov['weights'] = 0
    for i, name in enumerate(stocklist):
        df_port_cov[name] = df_cov[name] * \
            df_cov['weight']*df_cov.loc[i, 'weight']
        df_port_cov['weights'] += df_port_cov[name]
    port_var = df_port_cov['weights'].sum()

    portfolio_return = (wt_return)
    portfolio_std = port_var**(0.5)

    print(opt_weight)
    print(f'Max: {((portfolio_return + portfolio_std)*100):.2f} %')
    print(f'Min: {((portfolio_return - portfolio_std)*100):.2f} %')
    print('')
    print('')
    pf_return.append(((portfolio_return + portfolio_std)*100))
    pf_risk.append(((portfolio_return - portfolio_std)*100))
