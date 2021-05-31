# Dash packages
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import sd_material_ui as sdmui

from src.data_loading import *

# Stock symbol to be displayed as dropdown
stock_symbol_df = get_ticker_list()
stock_symbol_df['Stock_Symbol_Display'] = \
    stock_symbol_df['Name'] + ' (' + stock_symbol_df['Symbol'].astype(str) + ')'
stock_symbol_dict = dict(zip(stock_symbol_df['Symbol'], stock_symbol_df['Stock_Symbol_Display']))
stock_symbol_dict = [{'label': label, 'value': value} for value, label in stock_symbol_dict.items()]

###############################################################################
# LANDING PAGE LAYOUT
###############################################################################
layout = dbc.Container([

    html.H1('My LAW Project'),
    html.Hr(),
    sdmui.AutoComplete(id='home_dropdown_symbol', hintText='Select Stock Symbol', dataSource=stock_symbol_dict,
                       selectedValue=stock_symbol_dict[0]['value'],
                       maxSearchResults=10, filter='caseInsensitiveFilter'),
    html.Br(),
    html.H2(id='home_h2_selected_stock'),
    dbc.Row([
        dbc.Col([
            sdmui.Paper([
                dcc.Graph(id='home_viz_bollingerbands'),    
            ], zDepth=1),
        ], width=9),
        dbc.Col([
            sdmui.Paper([
                html.H5("TICKER"),
                html.Div(id='home_div_ticker_symbol',
                         style={'font-size': 'xx-large'}),
                html.Div(id='home_div_ticker_name',
                         style={'font-size': 'medium'}),
                html.Br(),
                html.Hr(),
                html.Br(),
                html.H5("LAST CLOSING"),
                html.Div(id='home_div_last_closing_price',
                         style={'font-size': 'xx-large'}),
                html.Br(),
                html.H5("RECOMMENDATION"),
                html.Div(id='home_div_recommendation',
                         style={'font-size': 'xx-large'}),
                html.Div(id='home_div_recommendation_subtext',
                         style={'font-size': 'medium'}),
                html.Br(),
                html.H5("DESCRIPTION"),
                html.Div(id='home_div_ticker_description',
                         style={'font-size': 'medium'}),
            ], zDepth=1, className='p-4')
        ])
    ]),
    html.Br(),
    html.H3("Stock Statistics:", style={'margin-left': '1em'}),
    sdmui.Paper([
        dbc.Row([
            # TODO: Replace with statistics
            dbc.Col([
                html.H4("BUY RANGE"),
                html.Div(id='home_div_buy_range', 
                         style={'font-size': 'xx-large'}),
            ], width=3),
            dbc.Col([
                html.H4("TAKE PROFIT"),
                html.Div(id='home_div_take_profit', 
                         style={'font-size': 'xx-large'}),
                html.Div(id='home_div_take_profit_subtext',
                         style={'font-size': 'medium'}),
            ], width=3),
            dbc.Col([
                html.H4("STOP LOSS"),
                html.Div(id='home_div_stop_loss',
                         style={'font-size': 'xx-large'}),
                html.Div(id='home_div_stop_loss_subtext',
                         style={'font-size': 'medium'}),
            ], width=3),
            dbc.Col([
                html.H4("RISK TO REWARD"),
                html.Div(id='home_div_risk_to_reward',
                         style={'font-size': 'xx-large'}),
            ], width=3)
        ]),
    ], zDepth=1, className='p-4'),
    html.Br(),

], className="mt-4")






