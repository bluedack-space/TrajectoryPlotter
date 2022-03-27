import numpy as np
import pymap3d as pm
import plotly.graph_objects as go
from PandasHandler import *

class TrajectoryPlotter:

    def __init__(self):
        print("This is Constructor")
        
    def __del__(self):
        print("This is Destructor")

    @staticmethod
    def getEarth(clr,imax=30): 
        latitude   = np.linspace( -90.0, 90.0, imax)
        longitude  = np.linspace(-180.0,180.0, imax)
        lat, lon   = np.meshgrid(latitude, longitude)

        x0  = np.zeros([imax,imax])
        y0  = np.zeros([imax,imax])
        z0  = np.zeros([imax,imax])
        alt = 0.0
        for i1 in range(imax):
            lat = latitude[i1]
            for i2 in range(imax):
                lon = longitude[i2]
                x0[i1,i2],y0[i1,i2],z0[i1,i2] = pm.geodetic2ecef(lat, lon, alt)

        x0 = x0/1000.0
        y0 = y0/1000.0
        z0 = z0/1000.0
    
        # Set up trace
        trace= go.Surface(x=x0, y=y0, z=z0, colorscale=[[0,clr], [1,clr]], hoverinfo='skip')
        trace.update(showscale=False)
        return trace

    @staticmethod
    def displayEarth(fig,filePathEarth='earth.xlsx',row=1,col=2):
        dfSet         = PandasHandler.readAllSheets_Excel(filePathEarth)
        df            = dfSet[0]
        Earth = TrajectoryPlotter.getEarth('#325bff',imax=40)
        fig.add_trace( go.Scatter3d( x=df["Trace 0, x"], y=df["Trace 0, y"], z=df["Trace 0, z"], mode='lines', marker=dict(size=1, color='grey'   ), name="", hoverinfo='skip'), row=row, col=col )
        fig.add_trace( go.Scatter3d( x=df["Trace 1, x"], y=df["Trace 1, y"], z=df["Trace 1, z"], mode='lines', marker=dict(size=1, color='grey'   ), name="", hoverinfo='skip'), row=row, col=col )
        fig.add_trace( Earth, row=row, col=col)
        fig.add_trace( go.Scatter3d( x=df["Trace 3, x"], y=df["Trace 3, y"], z=df["Trace 3, z"], mode='lines', marker=dict(size=1, color='white'  ), name="", hoverinfo='skip'), row=row, col=col )
        fig.update_layout(scene=dict(xaxis=dict(title="X-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
        fig.update_layout(scene=dict(yaxis=dict(title="Y-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
        fig.update_layout(scene=dict(zaxis=dict(title="Z-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
        fig.update_layout(scene=dict(bgcolor="black"))
        #fig.update_layout(showlegend=False)

