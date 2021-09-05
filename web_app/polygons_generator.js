polygons_v = []

function genPoly(coords) {
    arr = []
    lat = coords[0]
    lon = coords[1]
    for (var i = 0; i < sw.length; i++) {
        lat += sw[i][0] / 10000;
        lon += sw[i][1] / 10000;
        arr.push([lat, lon]);
    }

    polygons_v = [];
    for (var i = 0; i < 5; i++) {
        new_arr = [];
        for (var j = 0; j < arr.length; j++) {
            ll = [];
            if(j<arr.length){
                ll[0] = arr[j][0] + weigth(i);
                ll[1] = arr[j][1] - weigth(i);
                new_arr.push(ll);
            }else{
                ll[0] = arr[j][0] - weigth(i);
                ll[1] = arr[j][1] - weigth(i);
                new_arr.push(ll);
            }
        }
        polygons_v.push(new_arr);
    }
}
