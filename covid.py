#! /usr/bin/env python

import argparse
import os.path
import sys
import requests
import json
import plots_covid
from flask import Flask, render_template


# constants
URL = 'https://pomber.github.io/covid19/timeseries.json'
VALID_MODES = ['deaths', 'confirmed', 'recovered']
SAVEFILE = 'data/data.json'


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
    This function returns the appropriate arguments that are
    parsed by the user through the command line.
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
    parser.add_argument('-s', '--saved', action='store_true', 
                help='plot from last saved data')                
    args = parser.parse_args()
    return(args)  


def request_data():
    """
    request_data:
    Args: -
    Returns: data [json]
    This function requests all data from URL.
    """
    try:
        r = requests.get(URL)
    except requests.exceptions.RequestException as e:
        print(f'Request status: {r.status()}, exits due to: {e}')
        sys.exit(-1)
    data = r.json()

    # always keep backup of last-time requested
    with open(SAVEFILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    # create countries csv file
    if not os.path.isfile(COUNTRIES_CSV):
        create_countries_csv(data)

    return(data)


def load_data():
    """
    load_data:
    Args: -
    Returns: data [json]
    This function loads the json file where the
    data from the last request are stored
    """
    try:
        with open(SAVEFILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f'Will request data due to exception: {e}.')
        data = request_data()
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
    with open(plots_covid.COUNTRIES_CSV, 'w') as f:
        for cnt in countries:
            f.write(cnt)
            f.write('\n')


def main(args=None):
    """
    main:
    Args: -
    Returns: -
    This function calls the appropriate functions
    according to the parsed arguments.
    """

    if args == None:
        args = parse_arguments()

    # data mode
    if args.mode in VALID_MODES:
        mode = args.mode
    else:
        print(f'Invalid mode, will consider deaths.')
        mode = 'deaths'

    # from saved data or request again
    if args.saved:
        data = load_data()
    else:
        data = request_data()

    # countries selection
    if args.countries:
        plot_url = plots_covid.plot_mode(data, args.countries, args.fitting, mode)
        return(plot_url)
    else:
        print(f'No country(-ies) found. Please provide them.')


if __name__ == '__main__':
    detect_python_version()
    main()