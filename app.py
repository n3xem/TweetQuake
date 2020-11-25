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
    tweet_urls = list(set(request.args.getlist("name")))
    tweet_urls = [url for url in tweet_urls if re.match(
        r'^https://twitter.com/.*/status/([0-9]{10,})$', url)]

    quake_dics = []
    for n in tweet_urls:
        tweetid = feft.tweeturl2id(n)
        if tweetid == 0:
            continue
        tweet_time = feft.tweetid2time(tweetid)
        quake_dics.append(tweet_time2earthquake(tweet_time))

    return render_template("result.html", quake_dics=quake_dics, tweet_urls=tweet_urls)


if __name__ == '__main__':
    app.run()
