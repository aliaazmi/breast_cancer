#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
import plotly.express as px
import plotly.io as pio
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from dash.dependencies import Output, Input
import plotly.figure_factory as ff
import plotly.graph_objs as go
from jupyter_dash import JupyterDash
import dash_html_components as html
from dash_table import DataTable
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/aliaazmi/databreast/main/Raw_data_breast_cancer_2.csv')

df_filterd1 = df[df['STAGE'].isin(['I', 'II', 'III', 'IV'])]
fig1 = px.pie(df_filterd1, values='Count', names='STAGE',
             title='<b>Stage (n=893)</b>',
             labels ='<b> STAGE </b>', hole=.3, color_discrete_sequence=px.colors.diverging.curl,)
fig1.update_traces(textposition='inside', textinfo='percent+label+value')

df_filterd7 = df[df['Tumor_Grade'].isin(['1','2','3'])]
fig7 = px.pie(df_filterd7, values='Count', names='Tumor_Grade',
             title='<b>Tumor Grade (n=604)</b>',
             labels ='Tumor_Grade', color_discrete_sequence=px.colors.diverging.Tropic)
fig7.update_traces(textposition='inside', textinfo='percent+label+value', )

fig5 = go.Figure(go.Waterfall(
    name = "Year", orientation = "v",
    measure = ["relative", "relative", "relative", "relative",  "total"],
    x = ["<b>2019</b>", "<b>2020</b>", "<b>2021</b>","<b>2022-until August</b>","<b>Total</b>"],
    textposition = "outside",
    text = ["519", "596", "538", "391", "2044"],
    y = [519, 596, 538, 391,2044],
    decreasing = {"marker":{"color":"Maroon", "line":{"color":"red", "width":2}}},
    increasing = {"marker":{"color":"#1C4E80", "line":{"color":"#00F5FF", "width":3}}},
    totals = {"marker":{"color":"#EA6A47", "line":{"color":"#1C4E80", "width":3}}},
))

fig5.update_layout(
        title = "Breast Cancer Pt",
        showlegend = True,
    margin=dict(t=5, b=85) )

fig6 = go.Figure()
fig6.add_trace(go.Bar(
    x=['TNBC, n=173, 15.8%', 'HR-ve/HER2+ve, n=187, 17.1%', 'HR+ve/HER2+ve, n=303, 27.6%', 'HR+ve/HER2-ve, n=433, 39.5%', ],
    y=[173, 187, 303, 433 ],
    name='Female',
    marker=dict(
        color='#1C4E80',
        line=dict(color='#1C4E80', width=2)
    )
))
fig6.update_traces(textposition='inside', selector=dict(type='bar'))
fig6.update_layout(xaxis=dict(title_text='<b>HR/HER2</b>'), 
        margin=dict(t=5, b=80) )

pie1_graph = dcc.Graph (figure=fig7,
                       style= {'gridArea': 'pie1'})
pie2_graph = dcc.Graph (figure=fig1,
                       style= {'gridArea': 'pie2'})

bar1_graph = dcc.Graph (figure=fig5,
                      style={'gridArea': 'bar1'})
bar2_graph = dcc.Graph (figure=fig6,
                      style={'gridArea': 'bar2'})

container = html.Div([ bar1_graph, bar2_graph, pie1_graph, pie2_graph,],
                    style={'display': 'grid',
                          'gridTemplateAreas':'"bar1 bar1" "pie1 pie2 " "bar2 bar2"',
                            'gridTemplateColumns': '45vw 55vw',
                           'columnGap': '2px',})

app = Dash(__name__)

title = html.H2 ("Beacon Hospital's Breast Cancer Statistic (2019-2022-August)",
                style={
                      'fontFamily': 'verdana',
                      'textAlign': 'center',
                      }, 
                        id='dashTitle',
                        className="titles")

app.layout = html.Div([ 
    html.H2(title), 
    html.H3('Year'), container,
   
])

if __name__ == "__main__":
    app.run_server()
    
    

