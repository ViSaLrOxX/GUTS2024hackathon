'''
FLIGHT TRACKING WITH PYTHON AND OPEN AIR TRAFFIC DATA
by ideagora geomatics | www.geodose.com | @ideageo
'''
#IMPORT LIBRARY
import requests
import json
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import HoverTool,LabelSet,ColumnDataSource
from bokeh.tile_providers import get_provider, STAMEN_TERRAIN
import numpy as np
from bokeh.server.server import Server
from bokeh.application import Application
from bokeh.application.handlers.function import FunctionHandler

#FUNCTION TO CONVERT GCS WGS84 TO WEB MERCATOR
#DATAFRAME
def wgs84_to_web_mercator(df, lon="long", lat="lat"):
    k = 6378137
    df["x"] = df[lon] * (k * np.pi/180.0)
    df["y"] = np.log(np.tan((90 + df[lat]) * np.pi/360.0)) * k
    return df

#POINT
def wgs84_web_mercator_point(lon,lat):
    k = 6378137
    x= lon * (k * np.pi/180.0)
    y= np.log(np.tan((90 + lat) * np.pi/360.0)) * k
    return x,y

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

#COORDINATE RANGE IN WEB MERCATOR
x_range,y_range=([xy_min[0],xy_max[0]], [xy_min[1],xy_max[1]])

#REST API QUERY
user_name=''
password=''
# url_data='https://'+user_name+':'+password+'@opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)
url_data='https://opensky-network.org/api/states/all?'+'lamin='+str(lat_min)+'&lomin='+str(lon_min)+'&lamax='+str(lat_max)+'&lomax='+str(lon_max)

    
#FLIGHT TRACKING FUNCTION
def flight_tracking(doc):
    # init bokeh column data source
    flight_source = ColumnDataSource({
        'icao24':[],'callsign':[],'origin_country':[],
        'time_position':[],'last_contact':[],'long':[],'lat':[],
        'baro_altitude':[],'on_ground':[],'velocity':[],'true_track':[],
        'vertical_rate':[],'sensors':[],'geo_altitude':[],'squawk':[],'spi':[],'position_source':[],'x':[],'y':[],
        'rot_angle':[],'url':[]
    })
    
    # UPDATING FLIGHT DATA
    def update():
        response=requests.get(url_data).json()
        
        #CONVERT TO PANDAS DATAFRAME
        col_name=['icao24','callsign','origin_country','time_position','last_contact','long','lat','baro_altitude','on_ground','velocity',       
'true_track','vertical_rate','sensors','geo_altitude','squawk','spi','position_source']
       
        flight_df=pd.DataFrame(response['states']) 
        flight_df=flight_df.loc[:,0:16] 
        flight_df.columns=col_name
        wgs84_to_web_mercator(flight_df)
        flight_df=flight_df.fillna('No Data')
        flight_df['rot_angle']=flight_df['true_track']*-1
        icon_url='https:...' #icon url
        flight_df['url']=icon_url
        
        # CONVERT TO BOKEH DATASOURCE AND STREAMING
        n_roll=len(flight_df.index)
        flight_source.stream(flight_df.to_dict(orient='list'),n_roll)
        
    #CALLBACK UPATE IN AN INTERVAL
    doc.add_periodic_callback(update, 5000) #5000 ms/10000 ms for registered user . 
    
    #PLOT AIRCRAFT POSITION
    p=figure(x_range=x_range,y_range=y_range,x_axis_type='mercator',y_axis_type='mercator',sizing_mode='scale_width',plot_height=300)
    tile_prov=get_provider(STAMEN_TERRAIN)
    p.add_tile(tile_prov,level='image')
    p.image_url(url='url', x='x', y='y',source=flight_source,anchor='center',angle_units='deg',angle='rot_angle',h_units='screen',w_units='screen',w=40,h=40)
    p.circle('x','y',source=flight_source,fill_color='red',hover_color='yellow',size=10,fill_alpha=0.8,line_width=0)

    #ADD HOVER TOOL AND LABEL
    my_hover=HoverTool()
    my_hover.tooltips=[('Call sign','@callsign'),('Origin Country','@origin_country'),('velocity(m/s)','@velocity'),('Altitude(m)','@baro_altitude')]
    labels = LabelSet(x='x', y='y', text='callsign', level='glyph',
            x_offset=5, y_offset=5, source=flight_source, render_mode='canvas',background_fill_color='white',text_font_size="8pt")
    p.add_tools(my_hover)
    p.add_layout(labels)
    
    doc.title='REAL TIME FLIGHT TRACKING'
    doc.add_root(p)
    
# SERVER CODE
apps = {'/': Application(FunctionHandler(flight_tracking))}
server = Server(apps, port=8084) #define an unused port
server.start()
server.io_loop.add_callback(server.show, "/")  # Show the app in the browser (you can access at http://localhost:8084)
print("Starting Bokeh server at http://localhost:8084")
server.io_loop.start()  # This ensures the server runs and doesn't stop immediately
