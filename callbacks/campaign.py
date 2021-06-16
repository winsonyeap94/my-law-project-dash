import json
import requests
import pandas as pd
from datetime import datetime
from dash.dependencies import Input, Output, State
import dash_table


from app import app
from src.viz import *
from conf import loguru_logger as _logger

API_URL = "http://my-law-network-campaign:3000/run_optimisation/"


# ====================================================================================================
# Tactical Model Data Table Column Update
# ==================================================================================================== 

@app.callback(
    [Output('campaign-tab1-product-data-cost-datatable', 'columns'),
    Output('campaign-tab1-product-data-profit-datatable', 'columns'),
    Output('campaign-tab1-kpi-budget-div', 'children'),
    Output('campaign-tab1-kpi-roi-div', 'children')],
    [Input('campaign-tab1-cluster-data-datatable', 'data'),
    Input('budget-value', 'value'), Input('min-roi-value', 'value')],
    prevent_initial_call=True)

def update_datatable(cluster_data, budget, roi):
    # removing row with empty cells
    def filter_empty_cell(data):
        clean_data = []
        for row in data:
            # require that all elements in a row are specified
            if all([cell != '' for cell in row.values()]):
                clean_data.append(row)
        return clean_data

    cluster_data_clean = filter_empty_cell(cluster_data)
    clus_prod_cost_columns = [{'id': 'Product_Type_Cost', 'name': 'ProductType/Cost(RM)'}]
    clus_prod_profit_columns = [{'id': 'Product_Type_Profit', 'name': 'ProductType/Profit(RM)'}]
    for list_dic in cluster_data_clean:
        clus_prod_cost_columns.append({"id": list_dic['Cluster'], "name": list_dic['Cluster']})
        clus_prod_profit_columns.append({"id": list_dic['Cluster'], "name": list_dic['Cluster']})
    roi = '{:,.1f} %'.format(roi)
    budget = 'RM {:,.2f}'.format(budget)
    return [clus_prod_cost_columns, clus_prod_profit_columns, budget, roi]

# ====================================================================================================
# Tactical Model Output: Campaign Cluster Product Assignment Tables
# ====================================================================================================
@app.callback(
    [Output('campaign-tab1-opt-roi-div', 'children'),
    Output('campaign-tab1-opt-profit-div', 'children'),
    Output('campaign-tab1-opt-cost-div', 'children'),
    Output('campaign-tab1-results-datatable', 'children')],
    [Input('campaign-tab1-btn-run-optimisation', 'n_clicks')],
    [State('budget-value', 'value'), State('min-roi-value', 'value'),
    State('campaign-tab1-cluster-data-datatable', 'data'),
    State('campaign-tab1-product-data-datatable', 'data'),
    State('campaign-tab1-product-data-cost-datatable', 'data'),
    State('campaign-tab1-product-data-profit-datatable', 'data'),
    State('campaign-tab2-customer-data-datatable', 'data')],
    prevent_initial_call=True
)

# callback to display tactical model output
def cluster_marketing_allocation(
    n_click, budget, ROI, cluster_data, product_data, product_cost_data, product_profit_data, customer_data_costprofit):

    _logger.info(f"[customer_marketing_allocation] Tactical Model Initiated.")

    # removing row with empty cells
    def filter_empty_cell(data):
        clean_data = []
        for row in data:
            # require that all elements in a row are specified
            if all([cell != '' for cell in row.values()]):
                clean_data.append(row)
        return clean_data

    # Consolidating inputs into JSON for post request
    api_json = {
        "budget": budget,
        "roi": ROI,
        "cluster": filter_empty_cell(cluster_data),
        "product": filter_empty_cell(product_data),
        "cost": filter_empty_cell(product_cost_data),
        "profit": filter_empty_cell(product_profit_data),
        "cust_cost_profit": filter_empty_cell(customer_data_costprofit)
    }
    api_json = json.dumps(api_json)  # Converting dict to json, especially to cater for True/False json types
    _logger.debug(f"[customer_marketing_allocation] Tactical Model api_json --> {api_json}")

    # Making POST request to API
    _logger.debug(f"[customer_marketing_allocation] Making API call to {API_URL}")
    api_response = requests.post(API_URL, data=api_json).json()
    #_logger.debug(f"[customer_marketing_allocation] api_response --> {api_response}")
    
    # Converting results json to dataframes for visualisation
    _logger.debug(f"[customer_marketing_allocation] Converting JSON responses to pd.DataFrame")
    api_response = dict(api_response)

    # Converting KPIs for visualisation
    _logger.debug(f"[customer_marketing_allocation] Converting KPI values to dash column")
    tactical_expected_money = pd.DataFrame(api_response['tactical_expected_money'])
    optimal_roi = '{:,.1f} %'.format(tactical_expected_money['optimal_ROI'][0])
    optimal_profit = 'RM {:,.2f}'.format(tactical_expected_money['money_expected_profit'][0].astype(float))
    optimal_cost = 'RM {:,.2f}'.format(tactical_expected_money['money_expected_cost'][0].astype(float))
    #cost_budget_diff = '+/- {:,.2f}'.format(tactical_expected_money['increased_budget'][0].astype(float))

    # Converting cluster product assignment results dash table for visualisation
    _logger.debug(f"[customer_marketing_allocation] Converting Cluster Product Assignment JSON to datatable")
    clus_prod_data = api_response['cluster_product_assignment_data']
    cluster_product_assignment_data = pd.DataFrame(api_response['cluster_product_assignment_data']).reset_index(drop=True)
    clus_prod_columns = [{"name": i, "id": i, } for i in (cluster_product_assignment_data.columns)]
    table_output = dash_table.DataTable(
                        data=clus_prod_data, columns=clus_prod_columns,
                        style_as_list_view=True,
                        style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                        style_header={
                            'backgroundColor': '#20c997',
                            'fontWeight': 'bold'},)
    return [optimal_roi, optimal_profit, optimal_cost, table_output]

# ====================================================================================================
# Operational Model: Campaign Cluster Customer Product Assignment Tables
# ====================================================================================================
@app.callback(
    [Output('campaign-tab2-kpi-budget-div', 'children'),
    Output('campaign-tab2-kpi-roi-div', 'children'),
    Output('campaign-tab2-kpi-profit-div', 'children'),
    Output('campaign-tab2-kpi-cost-div', 'children'),
    Output('campaign-tab2-results-datatable', 'children')],
    [Input('campaign-tab2-btn-run-optimisation', 'n_clicks')],
    [State('budget-value', 'value'), State('min-roi-value', 'value'),
    State('campaign-tab1-cluster-data-datatable', 'data'),
    State('campaign-tab1-product-data-datatable', 'data'),
    State('campaign-tab1-product-data-cost-datatable', 'data'),
    State('campaign-tab1-product-data-profit-datatable', 'data'),
    State('campaign-tab2-customer-data-datatable', 'data')],
    prevent_initial_call=True
)

def customer_marketing_allocation(
    n_clicks, budget, ROI, cluster_data, product_data, product_cost_data, product_profit_data, customer_data_costprofit):

    start_time = datetime.now()
    _logger.info(f"[customer_marketing_allocation] Operation Model Initiated.")

    # removing row with empty cells
    def filter_empty_cell(data):
        clean_data = []
        for row in data:
            # require that all elements in a row are specified
            if all([cell != '' for cell in row.values()]):
                clean_data.append(row)
        return clean_data

    # Consolidating inputs into JSON for post request
    api_json = {
        "budget": budget,
        "roi": ROI,
        "cluster": filter_empty_cell(cluster_data),
        "product": filter_empty_cell(product_data),
        "cost": filter_empty_cell(product_cost_data),
        "profit": filter_empty_cell(product_profit_data),
        "cust_cost_profit": filter_empty_cell(customer_data_costprofit)
    }
    api_json = json.dumps(api_json)  # Converting dict to json, especially to cater for True/False json types
    _logger.debug(f"[customer_marketing_allocation] Operational Model api_json --> {api_json}")

    # Making POST request to API
    _logger.debug(f"[customer_marketing_allocation] Making API call to {API_URL}")
    api_response = requests.post(API_URL, data=api_json).json()
    #_logger.debug(f"[customer_marketing_allocation] api_response --> {api_response}")
    
    # Converting results json to dataframes for visualisation
    _logger.debug(f"[customer_marketing_allocation] Converting JSON responses to pd.DataFrame")
    api_response = dict(api_response)

    operational_expected_money = pd.DataFrame(api_response['operational_expected_money'])
    revised_budget = 'RM {:,.2f}'.format(pd.DataFrame(api_response['tactical_expected_money'])['money_expected_cost'][0].astype(float))
    optimal_roi = '{:,.1f} %'.format(operational_expected_money['customer_optimal_ROI'][0])
    optimal_profit = 'RM {:,.2f}'.format(operational_expected_money['customer_expected_profit'][0].astype(float))
    optimal_cost = 'RM {:,.2f}'.format(operational_expected_money['customer_expected_cost'][0].astype(float))

    # Converting cluster product customer assignment results dash table for visualisation
    _logger.debug(f"[customer_marketing_allocation] Converting Cluster Product Customer Assignment JSON to datatable")
    clus_prod_cust_data = api_response['cluster_product_customer_assignment_data']
    cluster_product_cust_assignment_data = pd.DataFrame(api_response['cluster_product_customer_assignment_data']).reset_index(drop=True)
    clus_prod_columns = [{"name": i, "id": i, } for i in (cluster_product_cust_assignment_data.columns)]
    table_output = dash_table.DataTable(
                        data=clus_prod_cust_data, columns=clus_prod_columns,
                        style_as_list_view=True,
                        style_cell={'padding': '5px',
                                'textAlign': 'center',
                                'font-family': 'arial'},
                        style_header={
                            'backgroundColor': '#20c997',
                            'fontWeight': 'bold'},
                        style_data_conditional=[
                            {
                                'if': {
                                    'filter_query': '{Selected} = 1',
                                },
                                'backgroundColor': '#f0ad4e',
                                'color': 'white',
                                'fontWeight': 'bold'
                            }, 
                            {
                                'if': {
                                    'column_id': 'Selected',},
                                    'display': 'None',
                            },
                        ],
                        style_header_conditional=[
                            {
                                'if': {
                                    'column_id': 'Selected',},
                                    'display': 'None',}
                        ],)
    return [revised_budget, optimal_roi, optimal_profit, optimal_cost, table_output]