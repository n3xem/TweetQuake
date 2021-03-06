const createLabel = (L, id, html, position) => {
    L.Control.label = L.Control.extend({
        onAdd: function (map) {
            let text = L.DomUtil.create('div');
            text.id = id;
            text.innerHTML = html;
            return text;
        },
        onRemove: function (map) { }
    });
    L.control.label = function (opts) {
        return new L.Control.label(opts);
    }
    L.control.label({ position: position }).addTo(map);
};

const createImg = (L, src, width, position) => {
    L.Control.img = L.Control.extend({
        onAdd: function (map) {
            let img = L.DomUtil.create('img');
            img.src = src;
            img.setAttribute("data-intro", "こんにちは！このサイトでは、あなたの地震観測ツイートからどの程度位置情報がバレてしまうかを調査することができます。");
            img.setAttribute("data-step", "1");
            img.style.width = width;

            return img;
        },
        onRemove: function (map) {
        }
    });
    L.control.img = function (opts) {
        return new L.Control.img(opts);
    }
    L.control.img({ position: position }).addTo(map);
};

const createForm = (L) => {
    L.Control.form = L.Control.extend({
        onAdd: function (map) {
            let text = L.DomUtil.create('div');
            text.id = "l-control-form";
            text.innerHTML = `<form action="/result" method="get" id="form">
    <input type="text" name="name" placeholder="Tweet URL" id="tweet_url">
    <button type="submit" id="tweet_url_submit">送信</button>
</form>
<input type="button" value="チュートリアルを見る" onClick="tutorial()">
`;
            return text;
        },
        onRemove: function (map) {
        }
    });
    L.control.form = function (opts) {
        return new L.Control.form(opts);
    }
    L.control.form({ position: 'topleft' }).addTo(map);
};