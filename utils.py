import numpy as np

#POINT
def wgs84_web_mercator_point(lon,lat):
    k = 6378137
    x= lon * (k * np.pi/180.0)
    y= np.log(np.tan((90 + lat) * np.pi/360.0)) * k
    return x,int(y)

def rescale_coordinates(x, y, max_x, max_y):
    ratio_x = x / 9300000
    ratio_y = y / 10000000
    return int(max_x * ratio_x), int(max_y * ratio_y)

if __name__ == "__main__":
    pass