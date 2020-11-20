let init = () => {
    let map = L.map('mapid');
    map.setView([38.40, 136], 5);
    L.tileLayer('https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png', {
        attribution: "<a href='https://maps.gsi.go.jp/development/ichiran.html' target='_blank'>地理院タイル</a>"
    }).addTo(map);
    L.control.scale({ maxWidth: 200, position: 'bottomright', imperial: false }).addTo(map);
    L.control.zoom({ position: 'bottomleft' }).addTo(map);
};