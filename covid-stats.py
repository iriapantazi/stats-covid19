#! /usr/bin/env python

import argparse
import os.path
import sys
import requests
import json
import matplotlib.pyplot as plt
import numpy as np


# constants
URL = 'https://pomber.github.io/covid19/timeseries.json'
COUNTRIES_CSV = 'countries.csv'


def detect_python_version():
    """
    """
    if sys.version_info.major < 3:
        print(f'Python {sys.version_info.major} '
                f'is not supported. Program exits.')
        sys.exit(-1)


def parse_arguments():
    """
    parse_arguments:
    Args: -
    Returns: args [str]
    This function returns the appropriate arguments.
    """
    parser = argparse.ArgumentParser(
                description='This program takes data concerning'
                'COVID-19 confirmed cases, and creates plots.'
                )
    parser.add_argument('-c', '--countries', nargs='+', 
                help='entrer the name(s) of country(-ies)')
    parser.add_argument('-d', '--deaths', action='store_true', 
                help='to plot deaths')
    parser.add_argument('-r', '--recovered', action='store_true', 
                help='to plot recovered')
    parser.add_argument('-o', '--confirmed', action='store_true', 
                help='to plot confirmed cases')
    args = parser.parse_args()
    return(args)  


def choose_title(mode):
    """
    choose_title:
    Args: mode [str]
    Returns: title [str]
    """
    if mode == 'deaths':
        return(f'Plot of number of cumulative deaths')
    elif mode == 'recovered':
        return(f'Plot of number of cumulative recovered cases')
    elif mode == 'confirmed':
        return(f'Plot of number of cumulative confirmed cases')



def request_data(entries, mode):
    """
    request_data:
    Args: entries [list], mode [str]
    Returns: -
    This function requests data of countries
    contained in entries list with the mode
    that has been parsed.
    """
    r = requests.get(URL)
    data = r.json()
    
    # create countries csv file
    if not os.path.isfile(COUNTRIES_CSV):
        create_countries_csv(data)

    # initiate plot
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_yscale('log')
    x = np.arange(len(data.get('Afghanistan')))

    # extract y-axis data
    for ent in entries:
        res = data.get(ent)
        if (res == None):
            print(f'There is no country named {ent}.'
                    f'Please refer to {COUNTRIES_CSV} for'
                    f'a list of valid countries.')
            continue
        mode_entries = []
        for dt in res:
            try:
                mode_num = int(dt.get(mode))
            except Exception as e:
                print(f'program breaks due to: {e}')
                sys.exit(-1)
            mode_entries.append(mode_num)
        plt.plot(x, mode_entries, 'o-',label=ent)
    plt.ylim(ymin=1.0)
    plt.legend(frameon=False)
    plt.title(choose_title(mode))
    plt.show()


def create_countries_csv(data):
    """
    create_countries_csv:
    Args: data [dist]
    Returns: -
    This function creates a csv file
    with the names of all countries if
    it does not exist.
    """
    countries = list(data.keys())
    with open(COUNTRIES_CSV, 'w') as f:
        for cnt in countries:
            f.write(cnt)
            f.write('\n')


def main():
    """
    main:
    Args: -
    Returns: -
    This function calls the appropriate
    functions according to the parsed
    arguments.
    """
    detect_python_version()

    args = parse_arguments()

    if args.deaths:
        mode = 'deaths'
    elif args.recovered:
        mode = 'recovered'
    elif args.confirmed:
        mode = 'confirmed'
    else:
        mode = 'deaths'
        print(f'No mode requested, will consider number of deaths.')


    if args.countries:
        request_data(args.countries, mode)


if __name__ == "__main__":
    main()
