# **Utility for COVID-19 data prediction**
---

This utility is a small program written in Python 
that produces plots for the data of COVID-19
available through: 
`https://pomber.github.io/covid19/timeseries.json`.

## **Getting started**

### **Prerequisites**
The program is written in Python 3.8 and can run 
with Python versions 3.6 and 3.7. Older versions
have not been tested, and the program
exits if Python 2.7 or older is detected.
It is suggested that the user creates a virtual environment. 
Such packages for creating and using virtual environments are 
[mkvirtualenv](https://realpython.com/python-virtual-environments-a-primer/) 
and [pyenv](https://realpython.com/intro-to-pyenv/).
After initialising a virtual environment, the user 
has to install the package requirements with the command 
`pip install -r requirements.txt`.


## **Information on input and output**
The program provides a  variation of arguments that can be parsed. 
These are:
1. `-c` for providing the country name(s).
2. `-m` for choosing from valid modes (deaths, confirmed, recovered).
3. `-f` for including fitting on the data (default=false).
These options are also available through the command 
`./covid-stats.py -h`.

## N.B. ##
- The plots start from day 0 (2020-01-22), and continue up to current date.
- When requesting data for countries like UK, use 'United Kingdom'.
- File `countries.csv` contains all valid countries for which data are provided.
- Fitting correction is still in progress.

### **Example input/output**
Requesting the number of deaths `./covid-stats.py -d -c Greece Italy`.
Exampple plots for cumulative number of confirmed cases and deaths
for three countries:

[image](img/plot.png "deaths")


## **Authors** 
If you have any suggestions/corrections, 
please contact [Iria Pantazi](iria.a.pantazi@gmail.com).


