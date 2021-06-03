import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc


# ================================================================================
# Tab 1: Strategic Campaign Planning
# ================================================================================
tab1_strategic_content = dbc.Card([

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
                         ] + [{'Cluster': '', 'Count': ''} for i in range(5)],
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
            html.H6("Product Data"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab1-product-data-datatable',
                    columns=(
                        [{'id': 'Product_Type', 'name': 'Product Type'},
                         {'id': 'Count', 'name': 'Count'},
                         {'id': 'Profit_Per_Unit', 'name': 'Profit Per Unit (RM)'},
                         {'id': 'Cost_Per_Unit', 'name': 'Cost Per Unit (RM)'}]
                    ),
                    data=[
                             {'Product_Type': 'P1', 'Count': 2, 'Profit_Per_Unit': 60, 'Cost_Per_Unit': 15},
                             {'Product_Type': 'P2', 'Count': 2, 'Profit_Per_Unit': 40, 'Cost_Per_Unit': 5},
                         ] + [{'Product_Type': '', 'Count': '', 'Profit_Per_Unit': '', 'Cost_Per_Unit': ''}
                              for i in range(5)],
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

    dbc.Button("Run Optimisation", id='campaign-tab1-btn-run-optimisation', className='campaign-btn m-4'),
    html.Br(),

    # ============================== Middle Section: KPIs ==============================
    html.H4("Campaign KPIs"),
    html.Hr(),
    dbc.Row([
        dbc.Col(width=1),
        dbc.Col(dbc.Card([
            html.H6("ROI"),
            html.Div("99.9%", id='campaign-tab1-kpi-roi-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(dbc.Card([
            html.H6("Profit"),
            html.Div("RM 100,000", id='campaign-tab1-kpi-profit-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(dbc.Card([
            html.H6("Cost"),
            html.Div("RM 10,000", id='campaign-tab1-kpi-cost-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(width=1),
    ]),

    html.Br(),
    # ============================== Bottom Section: Results ==============================
    html.H4("Optimisation Results"),
    html.Hr(),
    dbc.Row([
        dash_table.DataTable(id='campaign-tab1-results-datatable')
    ]),

    html.Br(),


], body=True)


# ================================================================================
# Tab 2: Tactical Campaign Planning
# ================================================================================
tab2_tactical_content = dbc.Card([

    # ============================== Top Section: Settings ==============================
    html.H4("Campaign Inputs"),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.H6("Customer Data"),
            html.Div(
                dash_table.DataTable(
                    id='campaign-tab2-customer-data-datatable',
                    columns=(
                        [{'id': 'Customer', 'name': 'Customer'},
                         {'id': 'Product', 'name': 'Product'},
                         {'id': 'Cost', 'name': 'Cost (RM)'},
                         {'id': 'Profit', 'name': 'Profit (RM)'}]
                    ),
                    data=[
                             {'Customer': 'C1', 'Product': 'P1', 'Cost': 20, 'Profit': 300},
                             {'Customer': 'C2', 'Product': 'P1', 'Cost': 30, 'Profit': 400},
                             {'Customer': 'C3', 'Product': 'P2', 'Cost': 25, 'Profit': 550},
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
            html.H6("ROI"),
            html.Div("99.9%", id='campaign-tab2-kpi-roi-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(dbc.Card([
            html.H6("Profit"),
            html.Div("RM 100,000", id='campaign-tab2-kpi-profit-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(dbc.Card([
            html.H6("Cost"),
            html.Div("RM 10,000", id='campaign-tab2-kpi-cost-div')  # You can put icons in this div too
        ], body=True, className='campaign-card')),
        dbc.Col(width=1),
    ]),

    html.Br(),
    # ============================== Bottom Section: Results ==============================
    html.H4("Optimisation Results"),
    html.Hr(),
    dbc.Row([
        dash_table.DataTable(id='campaign-tab2-results-datatable')
    ]),

    html.Br(),

], body=True)


# ================================================================================
# Overall Layout
# ================================================================================
layout = dbc.Container([

    html.H2('Campaign Optimisation'),
    html.Hr(),
    html.Br(),

    dbc.Tabs([
        dbc.Tab(tab1_strategic_content, label='Strategic Campaign Planning'),
        dbc.Tab(tab2_tactical_content, label='Tactical Campaign Planning'),
    ])

], className="mt-4")
