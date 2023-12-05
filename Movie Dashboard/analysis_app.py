#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov.14 18:12:28 2023

@author: huangrunzhe
"""

import dash

# Import css style
external_css = [
    "https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css",
    "http://raw.githack.com/ffzs/DA_dash_hr/master/css/my.css"
]

# Create an app and server
app = dash.Dash(__name__, external_stylesheets=external_css)
server = app.server

# Chart color
color_scale = ['#2c0772',
               '#3d208e',
               '#8D7DFF',
               '#CDCCFF',
               '#C7FFFB',
               '#ff2c6d',
               '#564b43',
               '#161d33',
               '#1f77b4',
               '#2171b5']