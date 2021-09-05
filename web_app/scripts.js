ymaps.ready(init);
var myPolygon;
var myMap;
function init() {
    myMap = new ymaps.Map("map", {
        center: [41.60844944, 41.68347095],
        zoom: 12,
        type: 'yandex#satellite'
    }, {
        searchControlProvider: 'yandex#search'
    });
    
    myMap.events.add('click', function (e) {
        var coords = e.get('coords');
        createPolygons(coords);
        console.log(coords);
    });
}
polygons = []
function createPolygons(coords) {
    genPoly(coords);
    for (var i = 0; i < polygons_v.length; i++) {
        myPolygon = new ymaps.Polygon([
            // Указываем координаты вершин многоугольника.
            polygons_v[i]
        ],
        // Описываем свойства геообъекта.
        {
            // Содержимое балуна.
            balloonContent: "Пожар"
        }, {
            // Описываем опции геообъекта.
            // Фоновое изображение.
            fillImageHref: 'media/fire_layer.png',
            // Тип заливки фоном.
            fillMethod: 'tile',
            opacity: 0.2,
            // Убираем видимость обводки.
            stroke: false
        }
        );
        polygons.push(myPolygon)
    }

    myMap.geoObjects.add(polygons[0]);
    myMap.setBounds(polygons[0].geometry.getBounds());
}