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
2. `-d` for plotting the cumulative deaths per day.
3. `-r` for plotting the cumulative recovered cases per day.
4. `-o` for plotting the cumulative confirmed cases per day.
These options are also available through the command 
`./covid-stats.py -h`.

The plots start from day 0 (2020-01-22), and continue up to current date.


### **Example input/output**
Requesting the number of deaths `./covid-stats.py -d -c Greece Italy`.
Exampple plots will follow.


## **Authors** 
If you have any suggestions/corrections, 
please contact [Iria Pantazi](iria.a.pantazi@gmail.com).


