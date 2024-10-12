import numpy as np
import math
#POINT


def wgs84_web_mercator_point(lon,lat):
    k = 6378137
    x= lon * (k * np.pi/180.0)
    y= np.log(np.tan((90 + lat) * np.pi/360.0)) * k
    return x,int(y)

#AREA EXTENT COORDINATE WGS84
lon_min,lat_min= -19.467443,-11.312829
lon_max,lat_max= 59.507757,36.830325
# -19.467443, 36.83032559604178
# 59.507757, -11.312829
#  55.820881, 23.501099
# 35.052984, 22.246543

#COORDINATE CONVERSION
xy_min=wgs84_web_mercator_point(lon_min,lat_min)
xy_max=wgs84_web_mercator_point(lon_max,lat_max)


def rescale_coordinates(longitude, latitude, mapWidth, mapHeight):

    x = (longitude+180)*(mapWidth/360)

    latRad = latitude*math.pi/180

    mercN = math.log(math.tan((math.pi/4)+(latRad/2)))
    y = (mapHeight/2)-(mapWidth*mercN/(2*math.pi))

    return x,y

if __name__ == "__main__":
    print(rescale_coordinates(466, 333,1000,700))