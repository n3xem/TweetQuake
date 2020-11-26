![TweetQuake](https://user-images.githubusercontent.com/40577403/100355445-1cd43000-3035-11eb-833b-77c5f58a572f.png)
# Description
![TweetQuake-Gif](https://raw.githubusercontent.com/wiki/n3xem/TweetQuake/images/tweetquake.gif)  
  
「地震きた」「ゆれた」などの地震を観測したツイートから、投稿者の位置情報の推定が出来るアプリです。  
各ツイートから、該当する地震を推測し、地震の震度観測データを重ね合わせることで、ある程度の位置情報の推定が出来ます。  
震度データは、気象庁の[震度データ](https://www.data.jma.go.jp/svd/eqev/data/bulletin/shindo.html)を加工し、利用しています。  
そのため、推測できる地震ツイートは、2010～2018年のものに限られます。
# install
```
$ pip install -r requirements.txt
```
# Usage
```
$ python app.py
```

そして、127.0.0.1:5000にアクセスしてください。
