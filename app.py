import folium
import find_earthquake_from_tweet as feft
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
    name = request.args.get("name")
    tweetid = feft.tweeturl2id(name)
    tweet_time = feft.tweetid2time(tweetid)
    quake_dic = tweet_time2earthquake(tweet_time)

    return render_template("result.html", quake_dic=quake_dic)


if __name__ == '__main__':
    app.run()
