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
}