import folium
import find_earthquake_from_tweet as feft
from flask import Flask, request, render_template

from find_earthquake_from_tweet import tweet_time2earthquake
app = Flask(__name__)


@app.route('/')
def hello_world():
    start_coords = (36.0, 138.0)
    folium_map = folium.Map(
        location=start_coords,
        zoom_start=5
    )
    folium_map.save('templates/map.html')
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

    m = folium.Map(
        location=[36, 138],
        zoom_start=5
    )
    intensity_colorcode = {
        "1": '#0c0e0e',
        "2": '#0f3b3d',
        "3": '#00269a',
        "4": '#5d4d0d',
        "A": '#c2b326',
        "B": '#b47518',
        "C": '#9f1b03',
        "D": '#770012',
        "7": '#86004b'
    }

    for dic in quake_dic["intensities"]:
        lat = dic["latitude"]
        lon = dic["longitude"]
        observ = dic["observ_point_num"]
        intensity = dic["intensity"]

        # folium.Marker([lat, lon], tooltip="観測点番号:" + observ + " 緯度:" +　str(lat) + " 経度:" + str(lon)).add_to(m)
        folium.CircleMarker(
            location=[lat, lon],
            radius=10,
            popup="観測点番号:" + observ + " 緯度:" + str(lat) + " 経度:" + str(lon),
            color=intensity_colorcode[intensity],
            fill=True,
            fill_color=intensity_colorcode[intensity]
        ).add_to(m)

    m.save('templates/map.html')
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
