var algorithm = function(source, target, datapoints){
    datapoints = datapoints.slice(datapoints.length/2);
    var between_points=[] 
    for (var i = 0; i < datapoints.length; i++) {
        if (datapoints[i][0]< source[0] && datapoints[i][0]>target[0] || datapoints[i][0]> source[0] && datapoints[i][0]<target[0]) {
        if (datapoints[i][0]< source[0] && datapoints[i][0]>target[0] || datapoints[i][0]> source[0] && datapoints[i][0]<target[0]) {

        between_points.push(datapoints)
        console.log('push');

      }
    }
   }
    function compare_lat(a,b) {
        return a[0]-b[0]
    }
    function compare_h(a,b) {
        return a[2]-b[2] 
    }
    between_points.sort(compare_h)
    var happy_points = between_points.slice(between_points.length-3) 
    console.log(happy_points);
    happy_points.sort(compare_lat)
    return happy_points
}

