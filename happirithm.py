# source :: [Lat, Long]
# target :: [Lat, Long] 
# data :: [Lat, Long, Score]
import math

def algo(source, target, data):
    solution = [0]
    direction = [target[0]-source[0], target[1]-source[1]]
    def magnitude(v):
        return math.sqrt(math.pow(v[0], 2) + math.pow(v[1], 2))
    distance = magnitude(direction)

    unit_direction = [direction[0]/distance, direction[1]/distance]

    def project(point):
        dot = point[0]*unit_direction[0]+point[1]*unit_direction[1]
        s = math.pow(magnitude(unit_direction), 2)
        return [dot/s * unit_direction[0], dot/s * unit_direction[1]]
    
    def error(point):
        projection = project(point)
        return magnitude([point[0]-projection[0], point[1]-projection[1]])

    def rank(a):
        x = project(a)
        return (x[0]-source[0])/unit_direction[0]
    def compare(a,b):
        return rank(a) - rank(b)

    data = sorted(data, key = rank);

    source.append(1); #Neutral score
    target.append(1); #Neutral score

    #Remove out of range items:
    while len(data) >0 and compare(data[0], source) < 0 :
        data.pop(0);
    while len(data) >0 and compare(data[len(data)-1], target) > 0 :
        data.pop();

    #Prepend Source vertex.
    data.insert(0,source);
    #Append Target vertex.
    data.append(target);

    #----------------------------------------------#
    # Data is now topologically sorted   
    # console.log("topologically sorted: ", data);
    #----------------------------------------------#
    def w(i,j):
        a = data[i]
        b = data[j]
        return math.sqrt(math.pow(b[0]-a[0], 2) + math.pow(b[1]-a[1], 2)) / b[2] + error(b)
    memo = {}
    child = {}
    def shortest(i):
        if i >= len(data)-1 :
            return 0 #Reached Target.
        if i in memo :
            return memo[i];

        best_length = float("inf");
        best_j = None
        for j in range(i+1 , len(data)): 
            cur_length = shortest(j) + w(i, j)
            if cur_length < best_length :
                best_length = cur_length
                best_j = j
        if best_j is None:
            return;
        memo[i] = shortest(best_j) + w(i,best_j)
        child[i] = best_j
        return memo[i]

    print(shortest(0))
    root = 0
    path = [data[root]]
    while root < len(data)-1 :
        root = child[root]
        path.append(data[root])
    return path;


print("Path: " + str(algo([0.,0.], [100.,100.], [[50, 75, 1], [80, 80, 2]])));