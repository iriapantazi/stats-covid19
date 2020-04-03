#! /usr/bin/env python

import argparse
import os.path
import sys
import requests
import json
import plots_covid 


# constants
URL = 'https://pomber.github.io/covid19/timeseries.json'
COUNTRIES_CSV = 'countries.csv'
VALID_MODES = ['deaths', 'confirmed', 'recovered']


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
    parser.add_argument('-m', '--mode', nargs='?', const='deaths', 
                help='mode to plot (deaths, confirmed, recovered)')
    parser.add_argument('-f', '--fitting', action='store_true', 
                help='include curve fitting')
    args = parser.parse_args()
    return(args)  


def request_data():
    """
    request_data:
    Args: -
    Returns: -
    This function requests all data from URL.
    """
    try:
        r = requests.get(URL)
    except requests.exceptions.RequestException as e:
        print(f'Request status: {r.status()}, exits due to: {e}')
        sys.exit(-1)
    data = r.json()
    
    # create countries csv file
    if not os.path.isfile(COUNTRIES_CSV):
        create_countries_csv(data)

    return(data)


def create_countries_csv(data):
    """
    create_countries_csv:
    Args: data [dist]
    Returns: -
    This function creates a csv file with the
    names of all countries if it does not exist.
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
    This function calls the appropriate functions
    according to the parsed arguments.
    """
    
    # python version
    detect_python_version()

    # argument parser
    args = parse_arguments()

    # data mode
    if args.mode in VALID_MODES:
        mode = args.mode
    else:
        print(f'Invalid mode, will consider deaths.')
        mode = 'deaths'

    # countries selection
    if args.countries:
        data = request_data()
        plots_covid.plot_mode(data, args.countries, args.fitting, mode)
    else:
        print(f'No country(-ies) found. Please provide them.')


if __name__ == "__main__":
    main()