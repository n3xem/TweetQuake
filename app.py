import find_earthquake_from_tweet as feft
import re
from flask import Flask, request, render_template

from find_earthquake_from_tweet import tweet_time2earthquake
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/map')
def map():
    return render_template('map.html')


@app.route("/result", methods=["GET"])
def result():
    overlap_observ_points = []
    observ_point_rep_num = {}
    tweet_urls = list(set(request.args.getlist("name")))
    tweet_urls = [url for url in tweet_urls if re.match(
        r'^https://twitter.com/.*/status/([0-9]{10,})$', url)]

    quake_dics = []
    for n in tweet_urls:
        tweetid = feft.tweeturl2id(n)
        tweet_time = feft.tweetid2time(tweetid)
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


if __name__ == '__main__':
    app.run()
