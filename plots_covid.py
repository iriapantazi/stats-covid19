#! /usr/bin/env python


import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from covid import COUNTRIES_CSV
from fit_functions import fit_exp_1


def title_sum(mode):
    """
    title_sum:
    Args: mode [str]
    Returns: title [str]
    """
    if mode == 'deaths':
        return(f'Total number of deaths')
    elif mode == 'recovered':
        return(f'Total number of recovered cases')
    elif mode == 'confirmed':
        return(f'Total number of confirmed cases')
    else:
        print(f'No valid mode was found. Program exits.')
        sys.exit(-1)


def title_sin(mode):
    """
    title_sin:
    Args: mode [str]
    Returns: title [str]
    """
    if mode == 'deaths':
        return(f'Number of deaths per day')
    elif mode == 'recovered':
        return(f'Number of recovered cases per day')
    elif mode == 'confirmed':
        return(f'Number of confirmed cases per day')
    else:
        print(f'No valid mode was found. Program exits.')
        sys.exit(-1)


def plot_mode(data, countries, fit, mode):
    """
    plot_mode:
    Args: data [dict], countries [list], fit [bool], mode [str]
    Returns: -
    """

    days = len(data.get('Afghanistan'))

    # initiate plot
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 2, 1)
    ax2 = fig.add_subplot(1, 2, 2)
    ax1.set_yscale('log')
    ax2.set_yscale('log')
    x = np.arange(days)
    x_fit = np.linspace(30, 60, 80)
    xmini = 20

    # extract y-axis data
    for cnt in countries:
        res = data.get(cnt)
        if (res == None):
            print(f'There is no country named {cnt}.'
                    f'Please refer to {COUNTRIES_CSV} for'
                    f'a list of valid countries.')
            continue
        mode_entries = []
        for dt in res:
            try:
                mode_num = int(dt.get(mode))
            except Exception as e:
                print(f'Program breaks due to: {e}')
                sys.exit(-1)
            mode_entries.append(mode_num)
            sing_entries = [mode_entries[i+1] - mode_entries[i] for i in range(len(mode_entries)-1)]
            sing_entries.insert(0, mode_entries[0])
        ax1.plot(x, mode_entries, 'o-', label=cnt)
        ax2.scatter(x, sing_entries, label=cnt)
        if fit:
            param = np.polyfit(x, mode_entries, 3)
            print(param)
            y_fit = [param[0]*i**3 + param[1]*i**2 +param[2]*i + param[3] for i in x_fit]
            ax1.plot(x_fit, y_fit, '--', label='fit '+cnt)

    ax1.set_ylim(1.0, None)
    ax2.set_ylim(1.0, None)
    ax1.set_xlim(xmini, None)
    ax2.set_xlim(xmini, None)
    ax1.legend(frameon=False, loc='upper left', prop={'size': 6})
    ax2.legend(frameon=False, loc='upper left', prop={'size': 6})
    ax1.set_title(title_sum(mode))
    ax2.set_title(title_sin(mode))
    #plt.show()
    plt.savefig('plot.png', bbox_inches='tight')
    plt.savefig('plot.pdf', bbox_inches='tight')