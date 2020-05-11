##Some useful links:

###Itertools / numpy / pandas
 
https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e
These are built-in and provide more methods to sort, operate on data collections. For example, compress, map_reduce etc.
Please, note that simple methods, such as filter, map, reduce are built-in to the language, you don’t need to import itertools
to use them.
 
If you install https://www.anaconda.com/distribution/ these packages and some others for data science will be available.
For example if you’d like to use pandas, you can install it via: 
conda install pandas

###More details:

https://www.scipy.org/install.html 
https://docs.anaconda.com/anaconda/install/

PyGTK seems to be not supported anymore (since 2011). 
Some info about other options  https://opensource.com/resources/python/gui-frameworks

####Mocking
To mock restful HTTP APIs you can use Wiremock: http://wiremock.org/.

The idea behind it is simple:
1. Start wiremock server in recording mode.
2. Setup a proxy so that all your HTTP requests go through Wiremock.
3. Run tests that make requests. 
4. After run wiremock will create json files with requests and responses recorded during test run. 
5. Start wiremock server in mock mode.
6. Wiremock will return responses instead of your server. 