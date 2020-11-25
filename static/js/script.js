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