from PandasHandler import *
from TrajectoryPlotter import *

import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots( rows=1, cols=2, specs=[[{"type":"scatter"},{"type":"scatter3d"}]] )

rowEath  = 1
colEarth = 2
rowPlot  = 1
colPlot  = 1

TrajectoryPlotter.displayEarth(fig,row=rowEath,col=colEarth)

filePathExcel_Data = 'TrajectoryAnalysis.xlsx'
dfSet_Data         = PandasHandler.readAllSheets_Excel(filePathExcel_Data)
sheetNames         = PandasHandler.getSheetNames_Excel(filePathExcel_Data)
index              = sheetNames.index('Run01')
df_Data            = dfSet_Data[index]

fig.add_trace( go.Scatter3d( x=df_Data["Position in ECEF-X[km]"], y=df_Data["Position in ECEF-Y[km]"], z=df_Data["Position in ECEF-Z[km]"], mode='lines', marker=dict(size=2, color='red'), line=dict(color='fuchsia',width=5), name="Trajectory"), row=rowEath, col=colEarth)

colNameX           = 'Time[min]'
colNameYList1      = ['Density[kg/m3]','Altitude[km]','MagFldInt in East[nT]','MagFldInt in North[nT]','MagFldInt in Up[nT]']
for i in range(len(colNameYList1)):
    colNameY = colNameYList1[i]
    fig.add_trace( go.Scatter(x= df_Data[colNameX],y= df_Data[colNameY], name=colNameY), row=rowPlot, col=colPlot )

fig.show()
fig.write_html("resultAsPlotly.html")
