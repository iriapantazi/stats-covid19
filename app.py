#! /usr/bin/env python

from flask import Flask
from flask import render_template
import io
import base64
import covid

app = Flask(__name__)


class Arguments:
    def __init__(self, countries=None, mode='deaths', fitting=False, saved=False):
        try:
            self.countries = countries.split(',')
        except Exception as e:
            print(f'{e}')
        self.mode = mode
        self.fitting = fitting
        self.saved = saved


@app.route('/')
def welcome():
    return('welcome to the project')


@app.route('/plot/anew/<string:ct>', methods=['GET'])
def plot_anew(ct):
    args = Arguments(countries=ct, saved=False)
    plot_url = covid.main(args)
    return(f'<img src="data:image/png;base64,{plot_url}">')
    #return(render_template('show_dynamic.html'), result=result)


@app.route('/plot/saved/<string:ct>', methods=['GET'])
def plot_saved(ct):
    args = Arguments(countries=ct, saved=True)
    plot_url = covid.main(args)
    return(f'<img src="data:image/png;base64,{plot_url}">')


@app.route('/show', methods=['GET', 'POST'])
def show():
    return(render_template('show_static.html'))


if __name__ == '__main__':
    app.run(debug = True, host='127.0.0.1', port='5000')