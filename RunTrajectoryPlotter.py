from PandasHandler import *
from TrajectoryPlotter import *

import plotly.express as px
import plotly.graph_objects as go

filePathExcel      = 'earth.xlsx'
dfSet              = PandasHandler.readAllSheets_Excel(filePathExcel)
df                 = dfSet[0]

filePathExcel_Data = 'TrajectoryAnalysis.xlsx'
dfSet_Data         = PandasHandler.readAllSheets_Excel(filePathExcel_Data)
sheetNames         = PandasHandler.getSheetNames_Excel(filePathExcel_Data)
index              = sheetNames.index('Run01')
df_Data            = dfSet_Data[index]

colNameX      = 'Time[min]'
colNameYList1 = ['Density[kg/m3]','Altitude[km]','MagFldInt in East[nT]','MagFldInt in North[nT]','MagFldInt in Up[nT]']

from plotly.subplots import make_subplots

colNames = list(df.columns)
imax     = len(colNames)

#fig = make_subplots(rows=2, cols=1)
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "scatter"},{"type": "scatter3d"}]]
)

Earth = TrajectoryPlotter.getEarth('#325bff',imax=40)

fig.add_trace( go.Scatter3d( x=df["Trace 0, x"], y=df["Trace 0, y"], z=df["Trace 0, z"], mode='lines', marker=dict(size=1, color='grey'   ), name="", hoverinfo='skip'), row=1, col=2 )
fig.add_trace( go.Scatter3d( x=df["Trace 1, x"], y=df["Trace 1, y"], z=df["Trace 1, z"], mode='lines', marker=dict(size=1, color='grey'   ), name="", hoverinfo='skip'), row=1, col=2 )
fig.add_trace( Earth, row=1, col=2)
fig.add_trace( go.Scatter3d( x=df["Trace 3, x"], y=df["Trace 3, y"], z=df["Trace 3, z"], mode='lines', marker=dict(size=1, color='white'  ), name="", hoverinfo='skip'), row=1, col=2 )
fig.add_trace( go.Scatter3d( x=df_Data["Position in ECEF-X[km]"], y=df_Data["Position in ECEF-Y[km]"], z=df_Data["Position in ECEF-Z[km]"], mode='lines', marker=dict(size=2, color='red'), line=dict(color='fuchsia',width=5), name="Trajectory"), row=1, col=2)
fig.update_layout(scene=dict(xaxis=dict(title="X-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
fig.update_layout(scene=dict(yaxis=dict(title="Y-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
fig.update_layout(scene=dict(zaxis=dict(title="Z-ECEF[km]", showgrid=True, showline=True, zeroline=False, backgroundcolor='black', color='grey', gridcolor='grey')))
fig.update_layout(scene=dict(bgcolor="black"))
#fig.update_layout(showlegend=False)

for i in range(len(colNameYList1)):
    colNameY = colNameYList1[i]
    fig.add_trace(go.Scatter(x= df_Data[colNameX],y= df_Data[colNameY], name=colNameY), row=1, col=1)

#for i in range(len(colNameYList2)):
#    colNameY = colNameYList2[i]
#    fig.add_trace(go.Scatter(x= df[colNameX],y= df[colNameY], name=colNameY), row=2, col=1)

fig.show()
fig.write_html("resultAsPlotly.html")