import re
import datetime as dt
from flask import Flask, request, render_template

from find_earthquake_from_tweet import tweet_time2earthquake, tweeturl2id, tweetid2time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/tutorial')
def tutorial():
    return render_template("index.html")


@app.route('/map')
def map():
    return render_template('map.html')


@app.route("/result", methods=["GET"])
def result():
    overlap_observ_points = []
    observ_point_rep_num = {}
    tweet_urls = list(set(request.args.getlist("name")))
    tweet_urls = [url for url in tweet_urls if validate(url)]

    tweet_ids = [tweeturl2id(tweet_url) for tweet_url in tweet_urls]
    tweet_times = [tweetid2time(tweet_id) for tweet_id in tweet_ids]

    quake_dics = []
    for tweet_time in tweet_times:
        earthquake = tweet_time2earthquake(tweet_time)
        quake_dics.append(earthquake)
        for intensity in earthquake["intensities"]:
            observ_point_rep_num.setdefault(
                intensity["observ_point_num"], {"num": 0, "latitude": intensity["latitude"], "longitude": intensity["longitude"]})
            observ_point_rep_num[intensity["observ_point_num"]]["num"] += 1

    for key in observ_point_rep_num.keys():
        if observ_point_rep_num[key]["num"] >= len(tweet_urls):
            overlap_observ_points.append(observ_point_rep_num[key])

    return render_template("result.html", quake_dics=quake_dics, tweet_urls=tweet_urls, overlap_observ_points=overlap_observ_points)


def validate(tweet_url):
    return (re.match(r'^\s*https://twitter.com/.*/status/([0-9]{10,})\s*$', tweet_url) and
            tweetid2time(tweeturl2id(tweet_url)) < dt.datetime(2019, 1, 1, 0, 0, tzinfo=dt.timezone(dt.timedelta(hours=9))))


if __name__ == '__main__':
    app.run()
