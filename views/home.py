import sd_material_ui as sdmui
import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Ol import Ol
import dash_bootstrap_components as dbc

from app import app


###############################################################################
# LANDING PAGE LAYOUT
###############################################################################
layout = dbc.Container([

    html.H1('Welcome to Our LAW Optimisation Dashboard'),
    html.Hr(),
    html.Br(),

    # ============================== Top Section: Warehouse ==============================
    dbc.Card([
        dbc.CardBody([
            html.Div('Use Case 1: Where should I place my warehouses ?', 
                     style={'color': '#17a2b8', 'fontSize': 30, 'font-weight': 'bold', 'text-align': 'center'}),
            html.Br(),
            dbc.Row([
                html.Div(
                    """
                    Due to the recent COVID-19 pandemic, our convenience store revenue has fallen due to restricted 
                    travelling by Malaysian citizens. People are now travelling on the streets less as compared to 
                    before.
                    """, className='mt-2'
                ),
                html.Br(),
                html.Div(
                    """
                    However, other businesses have gained from the changes brought upon by the pandemic. For example,
                    online shopping and delivery have become part of the new normal for many households in Malaysia.
                    """, className='mt-2'
                ),
                html.Br(),
                html.Div(
                    """
                    As a move to adapt to the new trend and to promote convenience store sales, PETRONAS has 
                    launched a new delivery service via our Setel app, where users can make purchases from nearby
                    Mesra stores and have them delivered to their doorstep.
                    """, className='mt-2'
                ),
                html.Br(),
                html.Div(
                    """
                    This however, requires upfront planning in terms of both warehouses (where to set them up and how
                    big do they need to be) and manpower (how many despatchers are required per station).
                    """, className='mt-2'
                ),
                html.Br(), html.Br(),
                html.Img(src=app.get_asset_url('Klang Valley.png'), className='center', style={'width': '50%'}),
                html.H5(
                    """
                    Today, we will explore how we can identify optimum warehouse locations and the number of 
                    despatchers to cater for the demand around Klang Valley.

                    The model inputs required are:
                    """, className='mt-4'
                ),
            ]),
            html.Ul(className='Lists'),
            html.Ol(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Candidate warehouse locations to be rented', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Despatcher manpower costs', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Delivery costs', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Other delivery constraints and settings (e.g., delivery speed, despatch volume limit, working hours)', 
                    style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Ul(className='Lists'),
        ]),
    ]),

    # ============================== Bottom Section: Campaign ==============================
    dbc.Card([
        dbc.CardBody([
            html.Div('Use Case 2: Who should I target to give the product offers ?', style={'color': '#f0ad4e', 'fontSize': 30, 'font-weight': 'bold', 'text-align': 'center'}),
            html.Br(),
            # dbc.Col([
            #     html.I(className='fas fa-solid fa-users fa-5x', style={'text-align': 'center', 'display': 'inline-block', 'width': '100%'}),
            #     # html.I(className='fas fa-solid fa-user-times fa-5x', style={'text-align': 'center', 'display': 'inline-block', 'width': '100%'}),
            #     # html.I(className='fas fa-solid fa-user-tag fa-5x', style={'text-align': 'center', 'display': 'inline-block', 'width': '100%'}),
            # ]),
            dbc.Row([
                dbc.Col([
                    html.Div(''),
                ]),
                dbc.Col([
                    html.I(className='fas fa-solid fa-user-check fa-5x')
                ]),
                dbc.Col([
                    html.I(className='fas fa-solid fa-user-times fa-5x'),
                ]),
                dbc.Col([
                    html.I(className='fas fa-solid fa-user-tag fa-5x'),
                ]),
            ]),
            html.Br(),
            html.H5('Companies across almost every industry are looking to optimize their marketing campaigns.  \
            Today, we’ll explore a marketing campaign optimization problem that is common in the banking and  \
            financial services industry, which involves determining which products to offer to individual customers \
            in order to maximize total expected profit while satisfying various business constraints.', style={'color': '#343a40', 'fontSize': 20}),
            html.Br(),
            html.H2('The model is divided into "Tactical Model" that provides a strategic marketing plan. The model inputs required are :', style={'color': '#343a40', 'fontSize': 20}),
            html.Ul(className='Lists'),
            html.Ol(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Number of Clusters and Count of Customers in Each Cluster', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Campaign Product Offers with Cost & Profit', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Campaign Budget (RM)', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Br(),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Campaign Minimum ROI (%)', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Ul(className='Lists'),

            html.Br(),
            html.H2('And also "Operational Model" that provides a more detailed planning that assist business decision in terms of which customers to offer. The model inputs required are :', style={'color': '#343a40', 'fontSize': 20}),
            html.Ul(className='Lists'),
            html.Li(className='fas fa-check-square fa-lg', style={'color': '#d9534f'}),
            html.I('  Expected Cost and Profit of Each Customer-Product pairing in Each Cluster', style={'color': '#343a40', 'fontSize': 20, 'text-align': 'center'}),
            html.Ul(className='Lists'),
            
        ]),
    ]),

], className="mt-4")






