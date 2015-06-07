/* source :: [Lat, Long] */
/* target :: [Lat, Long] */
/* data :: [Lat, Long, Score] */
data = []
var extract = function(raw){
    $(document).ready(function () {
    $.ajax({
        type: "GET",
        url: 'D:\Docs\Desktop\cached_tweets.csv',
        dataType: "csv",
        success: function (raw) {
            for row in raw:
                data.push([row[0], row[1], row[5]])
        }
    });
});
}

var algo = function(source, target, data){
    solution = [0];
    direction = [target[0]-source[0], target[1]-source[1]];
    var magnitude = function(v){
        return  Math.sqrt(Math.pow(v[0], 2) + Math.pow(v[1], 2));
    }
    distance = magnitude(direction);

    unit_direction = [direction[0]/distance, direction[1]/distance];

    var project = function(point){
        dot = point[0]*unit_direction[0]+point[1]*unit_direction[1];
        s = Math.pow(magnitude(unit_direction), 2);
        return [dot/s * unit_direction[0], dot/s * unit_direction[1]];
    }

    var error = function(point){
        var projection = project(point);
        return magnitude([point[0]-projection[0], point[1]-projection[1]]);
    }

    var compare = function(a,b){
        var rank= function(x){
            return (x[0]-source[0])/unit_direction[0]
        }
        return rank(project(a)) - rank(project(b));
    }

    data.sort(compare);

    source.push(1); //Neutral score
    target.push(1); //Neutral score

    //Remove out of range items:
    while(data.length>0 && compare(data[0], source) < 0) {
        data.shift();
    }
    while(data.length>0 && compare(data[data.length-1], target) > 0){
        data.pop();
    }

    //Prepend Source vertex.
    data.unshift(source);
    //Append Target vertex.
    data.push(target);

    /*----------------------------------*/
    /* Data is now topologically sorted */
    // console.log("topologically sorted: ", data);
    /*----------------------------------*/
    var w = function(i,j){
        var a = data[i];
        var b = data[j];
        return (Math.sqrt(Math.pow(b[0]-a[0], 2) + Math.pow(b[1]-a[1], 2))  + error(b)) / (Math.pow(b[2], 2))
    }
    memo = {};
    child = {};
    var shortest = function(i){
        if (i >= data.length-1){
            return 0;//Reached Target.
        }
        if( i in memo ){
            return memo[i];
        }
        var best_length = Number.POSITIVE_INFINITY;
        var best_j = null;
        var j;
        for (j = i+1; j < data.length; j++) { 
            var cur_length = shortest(j) + w(i, j);
            if(cur_length < best_length){
                best_length = cur_length;
                best_j = j;
            }
        }
        if(best_j === null){
            return;
        }
        memo[i] = shortest(best_j) + w(i,best_j);
        child[i] = best_j;
        return memo[i];
    }

    console.log(shortest(0));
    root = 0;
    path = [data[root]];
    while (root < data.length-1){
        root = child[root]
        path.push(data[root]);
    }
    return path;
}

console.log("Path: ", algo([0.,0.], [100.,100.], [[50, 75, 1], [80, 80, 2]]));