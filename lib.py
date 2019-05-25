from PIL import Image
from numpy import array
from numpy.linalg import norm
#get distance of closest mu
#param: 
#   rgb - the norm we want to compare against
#   n - the first mus we want to consider
def get_closest(rgb, n):
    global m
    #initialize to_return
    to_return = norm(rgb-m[0])
    for i in range(n):
        if norm(rgb-m[i]) < to_return:
            to_return = norm(rgb-m[i])
    return to_return