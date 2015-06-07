import numpy as np
X = np.genfromtxt("cut.csv",delimiter=",")


X = X[1:]

np.set_printoptions(precision=8)

with open("out.txt", "w") as text_file:
    text_file.write("[")
    for i in xrange(len(X)):
        text_file.write("[{},{},{}]".format(X[i][0],X[i][1],X[i][2]))
        if i != len(X)-1:
            text_file.write(",")
            text_file.write("\n")
    text_file.write("]")

#np.savetxt('out.txt',X,fmt='%15.8f')
