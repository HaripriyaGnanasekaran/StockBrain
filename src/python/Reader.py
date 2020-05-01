"""
Reader module has file reading classes.

List of Classes:  
StockReader: To read the stock history files.  
NewsReader: To read instant news articles from web. (has to be implemented).

"""
import pandas_datareader as ot_web

class StockReader:
    """
    StockReader reads stock from internet.

    Parameters:  
        1. st_source (str): a string of source name. eg. 'Yahoo' for Yahoo finance.
        2. st_sname (str): a string of stock name to read. eg. 'AAPL', 'RDS-A' etc.
        3. st_start (str): date from which stock data must be read. Format = 'yyyy-mm-dd'
        4. st_end (str): date till which stock data must be read. Format = 'yyyy-mm-dd'. 
    """

    def __init__(self, st_source, st_sname, st_start, st_end):

        self.st_sname = st_sname
        self.st_source = st_source
        self.st_start = st_start
        self.st_end = st_end 
        self.check_input()
        

    def check_input(self):
        """
        Check the input parameters.

        Unfortunately, we cannot accept all the inputs from the user.
        Though the GUI (when implemented) will constrain the inputs
        this method will currently check the user input.
        """
        ar_source = ['yahoo']
        ar_stocks = ['RDS-A']
        success = False
        if self.st_source in ar_source:
            if self.st_sname in ar_stocks:
                print('Input parameters accepted.')
                print('Attempting to read stock data.')
                success = True
            else: print('Rejected stock name.')
        else: print('Rejected source site.')
        return success
        

    def read_stock(self):
        """
        Reading stock using data_reader.
        """
        df_source = ot_web.DataReader(self.st_sname, self.st_source, self.st_start, self.st_end, retry_count=10, pause=0.1)
        return df_source 

    def read_file(self):
        pass

    def read_news(self, **kwargs):
        pass

    def read_webpage(self, **kwargs):
        pass

    def read_reports(self):
        pass

    def read_balance_sheet(self):
        pass

    def read_income_statement(self):
        pass

    def read_others(self):
        pass