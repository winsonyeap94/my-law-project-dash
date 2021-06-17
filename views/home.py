import dash_core_components as dcc
from dash_html_components.Ol import Ol
import dash_bootstrap_components as dbc
import dash_html_components as html
import sd_material_ui as sdmui


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
            html.Div('Use Case 1: Where to build warehouses ?', style={'color': '#17a2b8', 'fontSize': 30, 'font-weight': 'bold', 'text-align': 'center'}),
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






