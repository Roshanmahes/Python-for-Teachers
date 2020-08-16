import numpy as np
import plotly.graph_objs as go

import dash
import dash_core_components as dcc
import dash_html_components as html

# set up the chart
x = np.random.randn(500)
data = [go.Histogram(x=x)]
layout = go.Layout(
    title='This is a histogram about an IT survey',
    xaxis={'title':'How do you rate your satisfaction with Help Desk support?'},
    yaxis={'title':'Survey Respondents'}
)
fig = go.Figure(data=data, layout=layout)

# instantiate Dash
app = dash.Dash()
app.title = 'Deloitte Dash'

# app Layout
app.layout = html.Div([

    # header and logo
    html.Div([
        html.Img(
            src='https://www.deloitteforward.nl/wp-content/themes/deloitte/dist/images/logo.png',
            style={'height':'30px', 'padding-top': '10px', 'padding-left': '12px'}
        )], style={'height':'45px', 'backgroundColor': 'rgb(0,0,0)'}
    ),

    # title
    html.H4('Satisfaction survey', style={'text-align':'left'}),

    # body
    html.Div([
        dcc.Graph(
            figure=fig,
            style={'height':'400px', 'align':'center'}
        )]
    ),

    # footer
    dcc.Markdown('Code source: [Plotly Website](https://plot.ly/python/histograms/)'),
    html.Div([
        html.Div('Copyright © 2018',
        style={'color': 'rgb(255, 255, 255)', 'fontSize': 12, 'fontFamily':'Open Sans', 'font-weight': 'italic',
               'text-align':'right', 'vertical-align': 'bottom', 'padding-right':'10px'}
        )], style={'height':'30px', 'backgroundColor': 'rgb(0,0,0)'})
])

# Execute
app.run_server()
