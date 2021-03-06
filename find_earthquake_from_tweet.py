from datetime import timedelta
import json
import sys
import datetime as dt
import re


def tweeturl2id(url: str):
    match = re.match(
        r'^\s*https://twitter.com/.*/status/([0-9]{10,})\s*$', url)
    if match:
        return int(match.group(1))
    else:
        return 0


def tweetid2time(tweetid: int):
    unixtime = ((tweetid >> 22) + 1288834974657) / 1000.0
    return dt.datetime.fromtimestamp(
        unixtime, dt.timezone(dt.timedelta(hours=9)))


def tweet_time2earthquake(tweet_time):
    with open('record/i' + str(tweet_time.year)+'.json') as f:
        big_dic = json.load(f)

    near_dic = {}
    min_diff = timedelta.max
    JST = dt.timezone(timedelta(hours=+9), 'JST')

    for dic in big_dic["data"]:
        # 地震の時刻を取り出す
        dic_date_dt = dt.datetime \
                        .strptime(dic["time"], '%Y-%m-%d %H:%M:%S') \
                        .replace(tzinfo=JST)

        # ツイート時刻と地震の時刻を比較
        if tweet_time > dic_date_dt:
            td_abs = tweet_time - dic_date_dt
            if(td_abs < min_diff):
                min_diff = td_abs
                near_dic = dic

    return near_dic


if __name__ == '__main__':
    TWEET_URL = sys.argv[1]
    tweetid = tweeturl2id(TWEET_URL)
    tweet_time = tweetid2time(tweetid)
    tweet_time2earthquake(tweet_time)
