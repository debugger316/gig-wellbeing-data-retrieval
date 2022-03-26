from dataclasses import field
import datetime
import argparse
import requests
import csv
import json


parser = argparse.ArgumentParser(description='Get gig-worker data from Reddit')
parser.add_argument('json_files', metavar='files', type=str,
                    nargs='+', help='the json files to be parsed')

args = parser.parse_args()
for file in args.json_files:
    with open(file, 'r') as f:
        data_dict = json.load(f)
        begin_year = data_dict["beginYear"]
        begin_month = data_dict["beginMonth"]
        begin_day = data_dict["beginDay"]
        end_year = data_dict["endYear"]
        end_month = data_dict["endMonth"]
        end_day = data_dict["endDay"]

        timeStart = datetime.datetime(
            begin_year, begin_month, begin_day, 0, 0).timestamp()
        timeEnd = datetime.datetime(
            end_year, end_month, end_day, 0, 0).timestamp()

        sub = data_dict["sub"]
        keyword = data_dict["keyword"]

        def get_pushshift_data(after, before, sub, keyword):
            url = 'https://api.pushshift.io/reddit/search/submission/?&after=' + \
                str(after)+'&before='+str(before) + \
                '&subreddit='+str(sub)+'&q='+str(keyword)

            res = requests.get(url)
            data_list = res.json()['data']
            column_names = ['author', 'full_link', 'retrieved_on', 'selftext']
            with open('reddit_data.csv', 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(
                    f, fieldnames=column_names, extrasaction='ignore')
                writer.writerows(data_list)

        get_pushshift_data(timeStart, timeEnd, sub, keyword)
