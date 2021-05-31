import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


###############################################################################
# PAGE 2 LAYOUT
###############################################################################
layout = dbc.Container([

    html.H2('Warehouse Optimisation'),
    html.Hr(),
    html.Br(),

    # ============================== Top Section: Settings ==============================
    dbc.Card([
        dbc.CardHeader("Optimisation Settings"),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    # Optimisation Scenario
                    dbc.FormGroup([
                        html.H5("Optimisation Scenario"),
                        dbc.RadioItems(
                            options=[
                                {'label': '100% Demand Coverage', 'value': 1},
                                {'label': 'Maximise Profit', 'value': 2}
                            ],
                            value=1,
                            id='warehouse-radio-optimisation-scenario'
                        ),
                    ]),
                ], width=2, className='m-4'),
                dbc.Col([
                    # Add Delivery Time Constraint, Add Despatcher Hiring Cost, Add Delivery Cost
                    dbc.FormGroup([
                        html.H5("Additional Constraints or Considerations"),
                        html.H6("Maximum Delivery Hours"),
                        dbc.InputGroup([
                            dbc.InputGroupAddon(dbc.Checkbox('warehouse-checkbox-max-delivery-hours'),
                                                addon_type="prepend"),
                            dbc.Input(id='warehouse-input-max-delivery-hours', placeholder=3, type='number'),
                            dbc.InputGroupAddon("hr", addon_type='append'),
                        ], className='mb-3', size='sm'),
                        # Despatch Hiring Cost
                        html.H6("Despatch Hiring Cost"),
                        dbc.InputGroup([
                            dbc.InputGroupAddon(dbc.Checkbox('warehouse-checkbox-despatch-hiring-cost'),
                                                addon_type="prepend"),
                            dbc.Input(id='warehouse-input-despatch-hiring-cost', placeholder=2000, type='number'),
                            dbc.InputGroupAddon("RM/staff", addon_type='append'),
                        ], className='mb-3', size='sm'),
                        # Cost of Delivery
                        html.H6("Cost of Delivery"),
                        dbc.InputGroup([
                            dbc.InputGroupAddon(dbc.Checkbox('warehouse-checkbox-cost-of-delivery'),
                                                addon_type="prepend"),
                            dbc.Input(id='warehouse-input-cost-of-delivery', placeholder=3, type='number'),
                            dbc.InputGroupAddon("RM/hr", addon_type='append'),
                        ], className='mb-3', size='sm'),
                    ])
                ], width=4, className='m-4'),
                dbc.Col([
                    html.H5("Other settings"),
                    # Delivery Speed
                    html.H6("Delivery Speed"),
                    dbc.InputGroup([
                        dbc.Input(id='warehouse-input-delivery-speed', placeholder=60, type='number'),
                        dbc.InputGroupAddon("km/h", addon_type='append'),
                    ], className='mb-3', size='sm'),
                    # Despatch Volume Limit
                    html.H6("Despatch Volume Limit"),
                    dbc.InputGroup([
                        dbc.Input(id='warehouse-input-despatch-volume-limit', placeholder=2000, type='number'),
                        dbc.InputGroupAddon("ft3", addon_type='append'),
                    ], className='mb-3', size='sm'),
                    # Working Hours Per Day
                    html.H6("Working Hours"),
                    dbc.InputGroup([
                        dbc.Input(id='warehouse-input-working-hours', placeholder=12, type='number'),
                        dbc.InputGroupAddon("hr/day", addon_type='append'),
                    ], className='mb-3', size='sm'),
                    # Profit per Sales Volume
                    html.H6("Profit Per Sales"),
                    dbc.InputGroup([
                        dbc.Input(id='warehouse-input-profit-per-sales', placeholder=10, type='number'),
                        dbc.InputGroupAddon("RM/ft3", addon_type='append'),
                    ], className='mb-3', size='sm'),
                ], width=3, className='m-4'),
            ]),
        ]),
        dbc.CardFooter([
            dbc.Button("Run Optimisation")
        ])
    ]),

    # ============================== Bottom Section: Results ==============================
    html.Br(),
    dbc.Row([
        html.Div([
            dcc.Graph(id='geo_viz_warehouse', config={'displayModeBar': False}),
        ])
    ]),


], className="mt-4")

