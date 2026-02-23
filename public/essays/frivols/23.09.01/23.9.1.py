"""
Created on Sun Sep  3 00:35:25 2023

@author: Laplace
"""

from math import atan2, pi

h = 75
l = 75
d = 20 # head's width
x = 0
y = 0
thetas = []

def atg(y,x):
    # change the result range of atan2 to 0 - 2pi.
    if atan2(y,x) >= 0:
        res = atan2(y,x)
    else:
        res = atan2(y,x) + 2*pi
    return res
    
def integ(t):
    # sort the theta intervals by the left side and then
    # exam if there is overlapping and integrate each by each.
    res = sorted(t,key=lambda item: item[0])
    i = 0
    while i<len(res)-1:
        if res[i][1] >= res[i+1][0]:
            res[i:i+2] = [[res[i][0],res[i+1][1]]]
        else:
            i += 1
    return res

def counta(t,a,b):
    # calculate the length of each interval and add then together.
    res = 0
    i = 0
    ti = t[i]
    while ti[1]<=a:
        i += 1
        ti = t[i]
    j = len(t)-1
    tj = t[j]
    while tj[0]>=b:
        j -= 1
        tj = t[j]
    res = res + ti[1] - min(a,ti[0])
    res = res - tj[0] + min(b,tj[1])
    for k in range(i+1,j):
        res = res + t[k][1] - t[k][0]
    return res
    
# traverse all other people
# observer at row 3, col 7
for i in range(-8,7):
    for j in range(-12,3):
        if i==j==0:
            continue
        theta_r = atg(j*h-y,i*l+d/2-x)
        theta_l = atg(j*h-y,i*l-d/2-x)
        thetas.append([theta_l,theta_r])

thetasi = integ(thetas)
prob = (counta(thetasi,0,pi/6)+counta(thetasi,5*pi/6,2*pi))/(4/3*pi)

print(prob)