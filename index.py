import base64
import sd_material_ui as sdmui
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app, server

from callbacks import *
from views import (
    error, home, warehouse_overview, warehouse, campaign, campaign_overview
)

navBar = dbc.Navbar(
    id='navBar',
    children=[],
    sticky='top',
    color='primary',
    className='navbar navbar-expand-lg navbar-dark bg-primary',
)

################################################################################
# TITLE TO BE SHOWN ON BROWSER TAB
################################################################################
app.title = "LAW Optimisation Project"

################################################################################
# GENERAL LAYOUT
################################################################################
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        navBar,
        html.Div(id='pageContent')
    ])
], id='table-wrapper')


################################################################################
# HANDLE PAGE ROUTING - IF USER NOT LOGGED IN, ALWAYS RETURN TO LOGIN SCREEN
################################################################################
@app.callback(Output('pageContent', 'children'),
              [Input('url', 'pathname')])
def displayPage(pathname):
    if pathname == '/':
        return home.layout

    if pathname == '/home':
        return home.layout

    if pathname == '/warehouse-overview':
        return warehouse_overview.layout

    if pathname == '/warehouse':
        return warehouse.layout

    if pathname == '/campaign-overview':
        return campaign_overview.layout

    if pathname == '/campaign':
        return campaign.layout

    else:
        return error.layout


################################################################################
# ONLY SHOW NAVIGATION BAR WHEN A USER IS LOGGED IN
################################################################################
@app.callback(
    Output('navBar', 'children'),
    [Input('pageContent', 'children')])
def navBar(input1):
    logo_png = './assets/MyDashApp.png'
    logo_base64 = base64.b64encode(open(logo_png, 'rb').read()).decode('ascii')

    # Left side of Navbar
    common_navbar_contents = [
        dbc.Col([
            dbc.Row([
                html.Img(src='data:image/png;base64,{}'.format(logo_base64), height="65px", className='mr-3',
                         style={'-webkit-filter': 'drop-shadow(2px 2px 1px #222)',
                                'filter': 'drop-shadow(2px 2px 1px #222)',
                                'margin-left': '3em'}),
                dbc.NavbarBrand("LAW Optimisation Project", className="navbar-header", style={'color': '#222222'}),
                sdmui.Button(dbc.NavLink('Home', href='/home', className='p-1', style={'color': '#222222'}),
                             className='ml-4 mr-2', variant='text'),
                sdmui.Button(dbc.NavLink('Warehouse Problem Overview', href='/warehouse-overview', className='p-1',
                                         style={'color': '#222222'}),
                             className='mr-2', variant='text'),
                sdmui.Button(dbc.NavLink('Warehouse Optimisation', href='/warehouse', className='p-1',
                                         style={'color': '#222222'}),
                             className='mr-2', variant='text'),
                sdmui.Button(dbc.NavLink('Campaign Problem Overview', href='/campaign-overview', className='p-1',
                                         style={'color': '#222222'}),
                             className='mr-2', variant='text'),
                sdmui.Button(dbc.NavLink('Campaign Optimisation', href='/campaign', className='p-1',
                                         style={'color': '#222222'}),
                             className='mr-2', variant='text'),
            ], align='center')
        ], width=10),
    ]

    # Right Dropdown
    
    navBarContents = common_navbar_contents
    return navBarContents
    

server = app.server

if __name__ == '__main__':
    app.run_server(debug=False)
