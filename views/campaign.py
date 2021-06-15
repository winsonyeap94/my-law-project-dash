import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

# ================================================================================
# Tab 1: Tactical Campaign Planning
# ================================================================================
tab1_tactical_content = dbc.Card([

    # ============================== Top Section: Settings ==============================
    html.H4("Campaign Inputs"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H6("Cluster Data"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab1-cluster-data-datatable',
                    columns=(
                        [{'id': 'Cluster', 'name': 'Cluster'},
                         {'id': 'Count', 'name': 'Count'}]
                    ),
                    data=[
                             {'Cluster': 'k1', 'Count': 5},
                             {'Cluster': 'k2', 'Count': 5}
                         ] + [{'Cluster': '', 'Count': ''} for i in range(2)],
                    # Create additional blank rows for user input
                    editable=True,
                    style_as_list_view=True,
                    style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                    style_header={
                        'backgroundColor': '#ADD8E6',
                        'fontWeight': 'bold'
                    },
                ), className='p-4'
            )
        ]),
        dbc.Col([
            html.H6("Product Data: Count"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab1-product-data-datatable',
                    columns=(
                        [{'id': 'Product_Type', 'name': 'Product Type'},
                         {'id': 'Count', 'name': 'Count'}]
                    ),
                    data=[
                             {'Product_Type': 'p1', 'Count': 2},
                             {'Product_Type': 'p2', 'Count': 2},
                         ] + [{'Product_Type': '', 'Count': ''}
                             for i in range(2)],
                    # Create additional blank rows for user input
                    editable=True,
                    style_as_list_view=True,
                    style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                    style_header={
                        'backgroundColor': '#ADD8E6',
                        'fontWeight': 'bold'
                    },
                ), className='p-4'
            )
        ]),
        dbc.Col([
            html.H6("Product Data: Cost"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab1-product-data-cost-datatable',
                    columns=(
                        [{'id': 'Product_Type_Cost', 'name': 'ProductType/Cost(RM)'},
                         {'id': 'k1', 'name': 'k1'},
                         {'id': 'k2', 'name': 'k2'}]
                    ),
                    data=[
                             {'Product_Type_Cost': 'p1', 'k1': 200, 'k2': 300},
                             {'Product_Type_Cost': 'p2', 'k1': 100, 'k2': 200},
                         ] + [{'Product_Type_Cost': '', 'k1': '', 'k2': ''}
                             for i in range(2)],
                    # Create additional blank rows for user input
                    editable=True,
                    style_as_list_view=True,
                    style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                    style_header={
                        'backgroundColor': '#ADD8E6',
                        'fontWeight': 'bold'
                    },
                ), className='p-4'
            )
        ]),
        dbc.Col([
            html.H6("Product Data: Profit"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab1-product-data-profit-datatable',
                    columns=(
                        [{'id': 'Product_Type_Profit', 'name': 'ProductType/Profit(RM)'},
                         {'id': 'k1', 'name': 'k1'},
                         {'id': 'k2', 'name': 'k2'}]
                    ),
                    data=[
                             {'Product_Type_Profit': 'p1', 'k1': 2000, 'k2': 3000},
                             {'Product_Type_Profit': 'p2', 'k1': 1000, 'k2': 2000},
                         ] + [{'Product_Type_Profit': '', 'k1': '', 'k2': ''}
                              for i in range(2)],
                    # Create additional blank rows for user input
                    editable=True,
                    style_as_list_view=True,
                    style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                    style_header={
                        'backgroundColor': '#ADD8E6',
                        'fontWeight': 'bold'
                    },
                ), className='p-4'
            )
        ]),
    ]),

    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H6("Campaign Budget"),
            dbc.InputGroup([
                dbc.InputGroupAddon(
                    "RM", addon_type='prepend'),
                dcc.Input(
                    id='budget-value',
                    type='number',
                    value=200),
            ],className='mb-3', size='sm')], width=3),
        dbc.Col([
            html.H6("Campaign Minimum ROI"),
            dbc.InputGroup([
                dcc.Input(
                    id='min-roi-value',
                    type='number',
                    value=120),
                dbc.InputGroupAddon(
                    "%", addon_type='append'),
            ],className='mb-3', size='sm')], width=3),
    ]),
    dbc.Button("Run Optimisation", id='campaign-tab1-btn-run-optimisation', className='campaign-btn m-1'),
    html.Br(),


    # ============================== Middle Section: KPIs ==============================
    html.H4("Campaign KPIs"),
    html.Hr(),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-funnel-dollar'),
            html.H6("Initial Budget"), #dbc.CardImg(src='/assets/cash-coin.svg', style={'height':'20%', 'width':'20%'}),
            html.Div("RM 200.00", id='campaign-tab1-kpi-budget-div'),# You can put icons in this div too
        ], body=True, className='campaign-card', color="success", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-percentage'),
            html.H6("Minimum ROI"),
            html.Div("120.0 %", id='campaign-tab1-kpi-roi-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="warning", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-percentage'),
            html.H6("Optimal ROI"),
            html.Div("? %", id='campaign-tab1-opt-roi-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="info", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-users'),
            html.H6("Profit"),
            html.Div("RM ?", id='campaign-tab1-opt-profit-div')# You can put icons in this div too
        ], body=True, className='campaign-card', color="#6f42c1", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-dollar-sign'),
            html.H6("Cost"),
            html.Div("RM ?", id='campaign-tab1-opt-cost-div'),  # You can put icons in this div too
        ], body=True, className='campaign-card', color="danger", inverse=True)),
        dbc.Col(width=1),
    ]),

    html.Br(),
    # ============================== Bottom Section: Results ==============================
    html.H4("Optimisation Results"),
    html.Hr(),
    dbc.Col([
        html.Div(id='campaign-tab1-results-datatable')]),
        
], body=True)


# ================================================================================
# Tab 2: Operational Campaign Planning
# ================================================================================
tab2_operational_content = dbc.Card([

    # ============================== Top Section: Settings ==============================
    html.H4("Campaign Inputs"),
    html.Hr(),
    dbc.Col([
        dbc.Col([
            html.H6("Customer Data"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab2-customer-data-datatable',
                    columns=(
                        [{'id': 'Cluster', 'name': 'Cluster'},
                         {'id': 'Customer', 'name': 'Customer'},
                         {'id': 'Product', 'name': 'Product'},
                         {'id': 'Cost', 'name': 'Cost (RM)'},
                         {'id': 'Profit', 'name': 'Profit (RM)'}]
                    ),
                    data=[
                             {'Cluster': 'k1', 'Customer': 'c1', 'Product': 'p1', 'Cost': 205, 'Profit': 2050},
                             {'Cluster': 'k1', 'Customer': 'c2', 'Product': 'p1', 'Cost': 195, 'Profit': 1950},
                             {'Cluster': 'k1', 'Customer': 'c3', 'Product': 'p1', 'Cost': 200, 'Profit': 2000},
                             {'Cluster': 'k1', 'Customer': 'c4', 'Product': 'p1', 'Cost': 210, 'Profit': 2100},
                             {'Cluster': 'k1', 'Customer': 'c5', 'Product': 'p1', 'Cost': 190, 'Profit': 1900},
                             {'Cluster': 'k2', 'Customer': 'c6', 'Product': 'p1', 'Cost': 300, 'Profit': 3000},
                             {'Cluster': 'k2', 'Customer': 'c7', 'Product': 'p1', 'Cost': 290, 'Profit': 2900},
                             {'Cluster': 'k2', 'Customer': 'c8', 'Product': 'p1', 'Cost': 305, 'Profit': 3050},
                             {'Cluster': 'k2', 'Customer': 'c9', 'Product': 'p1', 'Cost': 310, 'Profit': 3100},
                             {'Cluster': 'k2', 'Customer': 'c10', 'Product': 'p1', 'Cost': 295, 'Profit': 2950},
                             {'Cluster': 'k1', 'Customer': 'c1', 'Product': 'p2', 'Cost': 105, 'Profit': 1050},
                             {'Cluster': 'k1', 'Customer': 'c2', 'Product': 'p2', 'Cost': 95, 'Profit': 950},
                             {'Cluster': 'k1', 'Customer': 'c3', 'Product': 'p2', 'Cost': 100, 'Profit': 1000},
                             {'Cluster': 'k1', 'Customer': 'c4', 'Product': 'p2', 'Cost': 110, 'Profit': 1100},
                             {'Cluster': 'k1', 'Customer': 'c5', 'Product': 'p2', 'Cost': 90, 'Profit': 900},
                             {'Cluster': 'k2', 'Customer': 'c6', 'Product': 'p2', 'Cost': 200, 'Profit': 2000},
                             {'Cluster': 'k2', 'Customer': 'c7', 'Product': 'p2', 'Cost': 190, 'Profit': 1900},
                             {'Cluster': 'k2', 'Customer': 'c8', 'Product': 'p2', 'Cost': 205, 'Profit': 2050},
                             {'Cluster': 'k2', 'Customer': 'c9', 'Product': 'p2', 'Cost': 210, 'Profit': 2100},
                             {'Cluster': 'k2', 'Customer': 'c10', 'Product': 'p2', 'Cost': 195, 'Profit': 1950},
                         ]  + [{'Cluster': '', 'Customer': '', 'Product': '', 'Cost': '', 'Profit': ''} for i in range(10)],
                    # Create additional blank rows for user input
                    editable=True,
                    style_as_list_view=True,
                    style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                    style_header={
                        'backgroundColor': '#ADD8E6',
                        'fontWeight': 'bold'
                    },
                ), className='p-4'
            )
        ]),
        dbc.Col(),
    ]),

    dbc.Button("Run Optimisation", id='campaign-tab2-btn-run-optimisation', className='campaign-btn m-4'),
    html.Br(),


    # ============================== Middle Section: KPIs ==============================
    html.H4("Campaign KPIs"),
    html.Hr(),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-funnel-dollar'),
            html.H6("Revised Budget"),
            html.Div("RM ?", id='campaign-tab2-kpi-budget-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="success", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-percentage'),
            html.H6("Optimal ROI"),
            html.Div("? %", id='campaign-tab2-kpi-roi-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="info", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-users'),
            html.H6("Profit"),
            html.Div("RM ?", id='campaign-tab2-kpi-profit-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="#6f42c1", inverse=True)),
        dbc.Col(dbc.Card([
            html.I(className='fas fa-dollar-sign'),
            html.H6("Cost"),
            html.Div("RM ?", id='campaign-tab2-kpi-cost-div')  # You can put icons in this div too
        ], body=True, className='campaign-card', color="danger", inverse=True)),
        dbc.Col(width=1),
    ]),

    html.Br(),
    # ============================== Bottom Section: Results ==============================
    html.H4("Optimisation Results"),
    html.Hr(),
    dbc.Col([
        html.Div(id='campaign-tab2-results-datatable')]),

], body=True)


# ================================================================================
# Overall Layout
# ================================================================================
layout = dbc.Container([

    html.H2('Campaign Optimisation'),
    html.Hr(),
    html.Br(),

    dbc.Tabs([
        dbc.Tab(tab1_tactical_content, label='Tactical Campaign Planning'),
        dbc.Tab(tab2_operational_content, label='Operational Campaign Planning'),
    ])

], className="mt-4")
