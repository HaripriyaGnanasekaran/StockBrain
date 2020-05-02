"""
Reader module has class Read.

List of Methods within class Read:  
read_stock: To read the stock history files.  
read_news: To read instant news articles from web. (has to be implemented).

"""
import pandas_datareader as fn_web

class Read:
    """
    Read provides different options for things that can be read.

    Parameters:  
        1. st_option (str): a string of different things that can be read. 

    Values:
    ['stock', 'news', 'web_page', 'report', 'balance_sheet', 'income_statement', 'other']
    """

    def __init__(self, st_option):

        self.st_option = st_option 
        self.check_input()
        

    def check_input(self):
        """
        Check the input parameters.

        Unfortunately, we cannot accept all the inputs from the user.
        Though the GUI (when implemented) will constrain the inputs
        this method will currently check the user input.
        """
        ar_option = ['stock', 'news', 'web_page', 'income_statement', 'balance_sheet', 'report', 'other']
        success = False
        if self.st_option in ar_option:
            success = True
        else: print('ValueError: {} not in the list of available options', self.st_option)
        return success
        

    def read_stock(self, st_source, st_sname, st_start, st_end):
        """
        Reading stock using data_reader.
    
        Parameters:  
        1. st_source (str): a string of source name. eg. 'Yahoo' for Yahoo finance.
        2. st_sname (str): a string of stock name to read. eg. 'AAPL', 'RDS-A' etc.
        3. st_start (str): date from which stock data must be read. Format = 'yyyy-mm-dd'
        4. st_end (str): date till which stock data must be read. Format = 'yyyy-mm-dd'.

        Returns: a dataframe of read stock data. 
        """

        df_source = fn_web.DataReader(st_sname, st_source, st_start, st_end, retry_count=10, pause=0.1)
        return df_source 

    def read_news(self, **kwargs):
        pass

    def read_webpage(self, **kwargs):
        pass

    def read_report(self):
        pass

    def read_balance_sheet(self):
        pass

    def read_income_statement(self):
        pass

    def read_others(self):
        pass