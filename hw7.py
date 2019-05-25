#!/usr/bin/python3
import sys
from PIL import Image
from numpy import array
from numpy.linalg import norm

bear = Image.open('pic.jpg')
pix_bear = bear.load()
print(bear.size)
print(pix_bear[0,0])

#find the 4 means
m = [array([147, 200, 250]), array([0, 0, 0]), array([137, 141,  57]), array([ 31,  70, 125])]

# #get distance of closest mu
# #param: 
# #   rgb - the norm we want to compare against
# #   n - the first mus we want to consider
# def get_closest(rgb, n):
#     global m
#     #initialize to_return
#     to_return = norm(rgb-m[0])
#     for i in range(n):
#         if norm(rgb-m[i]) < to_return:
#             to_return = norm(rgb-m[i])
#     return to_return

# #given an m with an initialized m[0]
# for n in range(1,4):
#     max_dist = -1
#     for i in range(bear.size[0]):
#         for j in range(bear.size[1]):
#             #find the closest mu we already have to the point i, j
#             #if the closest mu to the point distance is bigger than the current mu
#                 #set it to the current mu
#             closest = get_closest(array(pix_bear[i,j]),n)
#             if closest > max_dist:
#                 # print('closest:{}, max_dist:{}'.format(closest, max_dist))
#                 max_dist = closest
#                 m[n] = array(pix_bear[i,j])
#                 # print('m1-{}, i:{}, j:{}'.format(m[n],i,j))
# print(m)

#list of set
m_set = [[[-1,-1]],
        [[-1,-1]],
        [[-1,-1]],
        [[-1,-1]]]

#return an index to m
def get_closest_m(rgb):
    global m
    to_return = 0
    smallest = norm(rgb - m[0])
    for i in range(1, len(m)):
        if norm(rgb - m[i]) < smallest:
            smallest = norm(rgb - m[i])
            to_return = i
    return to_return

#compare each pixel with all the mus, see which yields the smallest distance
#   then add the pixel's coordinates to the m_x_set

for z in range(10):
    for i in range(bear.size[0]):
        for j in range(bear.size[1]):
            index = get_closest_m(array(pix_bear[i,j]))
            m_set[index].append([i,j])

    for i in range(len(m_set)):
        m_set[i].pop(0)
    # print(m_set)
    # print(len(m_set[0])+len(m_set[1])+len(m_set[2])+len(m_set[3]))

    # recalculate the mus
    # add up all the rgbs in the set

    for i in range(len(m_set)):
        vec_sum = array([0,0,0])
        for coor in m_set[i]:
            vec_sum += array(pix_bear[coor[0], coor[1]])
        m[i] = vec_sum / len(m_set[i])

    print(m)
