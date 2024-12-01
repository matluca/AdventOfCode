#!/usr/bin/env python3

# Script for getting the puzzle input
# For this to work, the browser_cookie3 library is needed, for retrieving the session cookie from the browser

import argparse
import browser_cookie3
import datetime
from datetime import date
import os
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-y", "--year", help="Year", type=int)
parser.add_argument("-d", "--day", help="Day", type=int)
args = parser.parse_args()


def get_year_and_day():
    target_date = date.today()
    if args.year is not None and args.day is not None:
        target_date = datetime.datetime(args.year, 12, args.day)
    y, m, d = target_date.year, target_date.month, target_date.day
    if int(y) < 2015 or int(y) > int(date.today().year):
        print("Invalid year")
        sys.exit(1)
    if int(m) != 12:
        print("Invalid month")
        sys.exit(1)
    if int(d) < 1 or int(d) > 25:
        print("Invalid day")
        sys.exit(1)
    return y, d


if __name__ == '__main__':
    year, day = get_year_and_day()
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    cj = browser_cookie3.firefox(domain_name='adventofcode.com')
    resp = requests.get(url, cookies=cj)
    if day < 10:
        day = f'0{day}'
    if resp.status_code != 200:
        print("Could not get input: ", resp)
        print(resp.content.decode('utf-8'))
        sys.exit(1)
    dirname = os.path.dirname(__file__)
    out_file = open(os.path.join(dirname, f'{year}/{day}/input.txt'), "w")
    print(resp.content.decode('utf-8'), file=out_file)
