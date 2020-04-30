# Developer Guidelines
Please create your own branch and start adding features that might benifit the program. Once you test all the features, test it with the existing unit tests from master branch. If unit testing is successful make a pull request!

# Contents
<!-- vscode-markdown-toc -->
* 1. [Variable definition](#Variabledefinition)
	* 1.1. [Variable nomenclature](#Variablenomenclature)
* 2. [Syntax and formatting](#Syntaxandformatting)
* 3. [Module definitions](#Moduledefinitions)

<!-- vscode-markdown-toc-config
	numbering=true
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

##  1. <a name='Variabledefinition'></a>Variable definition

1. Please adhere to the variable definitions as follows. Use small case letters. eg. ```stock, quote, train.``` 
2. While using a variable name with two or more parts combine them with an underscore "```_```". eg. ``` stock_price, quote_today, train_stock_for_numerical_results. ```
3. Capital letters, spaces, periods etc. are forbidden to be used in variable names. Such violations will lead to a rejected code piece during review.

###  1.1. <a name='Variablenomenclature'></a>Variable nomenclature

```
Variable name				Type

it_name					Integer 
ft_name					Float
st_name					String
lt_name					list
tp_name					tuple
dt_name					dictionary

df_name					pandas.DataFrame
ar_name					numpy.array
ot_name					objects of classes/modules
ot_pd					pandas object
ot_np					numpy object
ot_plt					matplotlib.pyplot object 
ot_sns					seaborn object 

it_name_lastname			Integer with a two names
it_length_array1			Array 1 length stored as integer
it_length_array2			Array 2 length stored as integer
tp_shape_df_source			Tuple storing shape of pandas.DataFrame called source.

```
1. All dataframes will be named as ```df_variablename```
2. All numpy arrays will be named as ```ar_variablename```
3. All integer, float and string objects will be named as ```in_, ft_, st_```
4. ```pandas object``` should be imported as ```pd``` 
5. ```numpy``` object should be imported as ```np ```
6. ```matplotlib.pyplot``` should be imported as ```plt``` 

##  2. <a name='Syntaxandformatting'></a>Syntax and formatting

1. Follow python enhancement propsal ([PEP 8](https://www.python.org/dev/peps/pep-0008/)) guidlines.
2. For StockBrain 0.0.0, every code will be placed in a single file named as ``` stock_brain_0_0_0.py ```. 

##  3. <a name='Moduledefinitions'></a>Module definitions

1. Module names should start with Upper case letter and continue with lower case letters. To avoid confusion with existing python modules we make our modules as verbs (since they perfom a action). eg. ``` Reader, Writer, Downloader, Cleaner,  Plotter, Printer, Solver, Modeller, Executer, Validator, Predictor.```

Take a look at the existing ```src/python/*.py``` to get an idea about naming classes and functions (methods). Classes are usually named using FirstnameLastname convention. Methods/functions are named completely in smaller cases with ```_``` connecting two or more words.

