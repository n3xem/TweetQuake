var tileLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="http://osm.org/copyright">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
});
var map = L.map('mapid', {
    center: [36, 140],
    zoom: 5,
    layers: [tileLayer],
});
map.zoomControl.setPosition("bottomright");

createForm(L);

let tweet_url_cnt = 0;

let tutorial = () => {
    introJs().setOptions({
        steps: [
            {
                intro: "TweetQuakeへようこそ！<br> このサイトでは、あなたの地震観測ツイートからどの程度位置情報がバレてしまうかを調査することができます。"
            },
            {
                intro: "今からこのサイトの使い方について説明します。"
            },
            {
                intro: "まずは、サイトを使う前に、あなたの「2018年までの地震観測ツイート」をいくつか探します。<br> \
                        ツイート検索で、 <b>from:自分のID until:2018-12-31 ゆれ</b> などで検索すると見つかるかもしれません。<br>（\
                        2018年までに限定しているのは、使っている震度データが、2018年までの物だからです。）<img src=\"static/images/tutorial-search.gif\">"
            },
            {
                intro: "見つかったら、このサイトでの作業に移ります。"
            },
            {
                element: document.querySelector('#tweet_url'),
                intro: "このボックスにURLを入力します。",
                position: 'bottom'
            },
            {
                element: document.querySelector('#tweet_url_submit'),
                intro: "このボタンを押します。",
                position: 'bottom'
            },
            {
                intro: "すると、地図上にツイートから予測された地震の観測点が表示されるはずです。<br>では、試しに私が見本を見せましょう。"
            },
            {
                element: document.querySelector('#tweet_url'),
                intro: "このボックスにURLを入力します。",
                position: 'bottom'
            },
            {
                element: document.querySelector('#tweet_url_submit'),
                intro: "このボタンを押します。",
                position: 'bottom'
            }
        ],
        exitOnOverlayClick: false
    }).onchange((targetElement) => {
        let tweet_url = "https://twitter.com/ID/status/1046965248379510785";

        let textbox_input = () => {
            console.log(tweet_url);
            if (tweet_url === '') {
                return;
            }
            tweet_url_element = document.querySelector('#tweet_url');
            tweet_url_element.value = tweet_url_element.value + tweet_url.slice(0, 1);
            tweet_url = tweet_url.slice(1);
            setTimeout(textbox_input, 30);
        }
        console.log("targetElement:" + targetElement.id);
        switch (targetElement.id) {
            case "tweet_url":
                if (tweet_url_cnt == 1) {
                    targetElement.value = "";
                    setTimeout(textbox_input, 30);
                } else {
                    targetElement.value = "";
                    tweet_url_cnt++;
                }
                break;
        }
    }).oncomplete(() => {
        window.location.href = "/result?name=https%3A%2F%2Ftwitter.com%2FID%2Fstatus%2F1046965248379510785&tutorial=2";
    }).start();
}

if (RegExp('tutorial', 'gi').test(window.location.pathname)) {
    tutorial();
}
