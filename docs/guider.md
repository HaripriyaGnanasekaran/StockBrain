# Developer Guidelines

# Contents
<!-- vscode-markdown-toc -->
* 1. [About StockBrain](#AboutStockBrain)
* 2. [Variable definition](#Variabledefinition)
	* 2.1. [Variable nomenclature](#Variablenomenclature)
* 3. [Syntax and formatting](#Syntaxandformatting)
* 4. [Module definitions](#Moduledefinitions)
* 5. [Copyright](#Copyright)
* 6. [Contact](#Contact)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='AboutStockBrain'></a>About StockBrain
StockBrain 0.0.0 is the beta version of DeepLearning algorithm to predict the stock price. We demonstrate the ability of the model over NYSE:RDS.A (Royal Dutch Shell A). StockBrain is programmed in [Python 3.8.2](https://www.python.org) and requires the following packages: [keras](https://keras.io/), [scipy](https://www.scipy.org/), [scikit-learn](https://scikit-learn.org/stable/), [pandas](http://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/). This module requires a backend package like [Tensorflow](https://www.tensorflow.org/), [Theano](http://deeplearning.net/software/theano/) or [CNTK](https://docs.microsoft.com/en-us/cognitive-toolkit/). We recommend to use Theano backend. Keras uses tensorflow by default. To change the keras backend visit [Keras website](https://www.keras.org)

Tested on.  
* OS: Windows 10  
* Processor: Intel Pentium 4415Y, 1.6 MHz, 2 cores, 4 processors  
* Python: 3.8.2 64-bit  
* Keras: 2.3.4  
* Theano: 1.0.4  

##  2. <a name='Variabledefinition'></a>Variable definition

1. Please adhere to the variable definitions as follows. Use small case letters. eg. ```stock, quote, train.``` 
2. While using a variable name with two or more parts combine them with an underscore "```_```". eg. ``` stock_price, quote_today, train_stock_for_numerical_results. ```
3. Capital letters, spaces, periods etc. are forbidden to be used in variable names. Such violations will lead to a rejected code piece during review.

###  2.1. <a name='Variablenomenclature'></a>Variable nomenclature

1. All dataframes will be named as ```df_variablename```
2. All numpy arrays will be named as ```ar_variablename```
3. All integer, float and string objects will be named as ```in_, ft_, st_```
4. ```pandas object``` should be imported as ```pd``` 
5. ```numpy``` object should be imported as ```np ```
6. ```matplotlib.pyplot``` should be imported as ```plt``` 

##  3. <a name='Syntaxandformatting'></a>Syntax and formatting

1. Follow python enhancement propsal ([PEP 8](https://www.python.org/dev/peps/pep-0008/)) guidlines.
2. For StockBrain 0.0.0, every code will be placed in a single file named as ``` stock_brain_0_0_0.py ```. 

##  4. <a name='Moduledefinitions'></a>Module definitions

1. Module names should be short and all lower case. To avoid confusion with existing python modules we make our modules as verbs (since they perfom a action). eg. ``` reader, writer, downloader, cleaner,  plotter, printer, solver, modeller, executer.```
3. Try to avoid module names with more than one word. If necessary used "```_```". eg. ```place_holder, data_cleaner, array_sorter.```
2. PEP places a naming format for classes as ClassName

##  5. <a name='Copyright'></a>Copyright

Currently StockBrain is a propreitary algorithm. If you, somehow, received a copy of it, it probably means the main algorithm (solver) is either modified or removed or replaced with a duplicate one. We refer to this modified/replaced/removed part as ```place_holder ``` This can obviously be realized through the results. StockBrain results will completely differ from the ```place_holder``` results.

##  6. <a name='Contact'></a>Contact 
StockBrain is a brainchild of Ramanathan Varadharajan (myself). It was started in the year of 2020. During this period I was finalizing my Ph.D. in Pysical Chemistry at [Wageningen University and Research Center.](https://www.wur.nl) My reserach primarily forcussed on Self consistent field modelling of oil/water interfaces within the [Pysical Chemistry and Soft Matter.](https://www.wur.nl/en/Research-Results/Chair-groups/Agrotechnology-and-Food-Sciences/Physical-Chemistry-and-Soft-Matter/Research.htm). To contact me, send an email to ramanathan.varadharajan@outlook.com 
