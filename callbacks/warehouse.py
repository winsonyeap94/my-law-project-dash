import dash
import json
import requests
import pandas as pd
from datetime import datetime
from dash.dependencies import Input, Output, State

from app import app
from src.viz import *
from conf import loguru_logger as _logger

API_URL = "http://my-law-network:6128/run_optimisation/"


# ====================================================================================================
# Warehouse Allocation Map
# ====================================================================================================
@app.callback(
    Output('geo_viz_warehouse', 'figure'),
    [Input('warehouse-btn-run-optimisation', 'n_clicks')],
    [State('warehouse-radio-optimisation-scenario', 'value'),
     State('warehouse-checkbox-max-delivery-hours', 'checked'), State('warehouse-input-max-delivery-hours', 'value'),
     State('warehouse-checkbox-despatch-hiring-cost', 'checked'), State('warehouse-input-despatch-hiring-cost', 'value'),
     State('warehouse-checkbox-cost-of-delivery', 'checked'), State('warehouse-input-cost-of-delivery', 'value'),
     State('warehouse-input-delivery-speed', 'value'), State('warehouse-input-despatch-volume-limit', 'value'),
     State('warehouse-input-working-hours', 'value'), State('warehouse-input-profit-per-sales', 'value')]
)
def viz_warehouse_allocation(
    n_clicks, optimisation_scenario, add_delivery_hrs, max_delivery_hrs, add_despatch_hiring_cost, despatch_hiring_cost,
    add_cost_of_delivery, cost_of_delivery, delivery_speed, despatch_volume_limit, working_hours, profit_per_sales
):

    start_time = datetime.now()
    _logger.info(f"[viz_warehouse_allocation] Initiated.")

    # Consolidating inputs into JSON for post request
    api_json = {
        "optimisation_scenario": optimisation_scenario,
        "add_delivery_time_constraint": False if add_delivery_hrs is None else True,
        "add_despatcher_hiring_cost": False if add_despatch_hiring_cost is None else True,
        "add_delivery_cost": False if add_cost_of_delivery is None else True,
        "despatch_hiring_cost": despatch_hiring_cost,
        "delivery_speed": delivery_speed,
        "despatch_volume_limit": despatch_volume_limit,
        "cost_of_delivery": cost_of_delivery,
        "working_hours_per_day": working_hours,
        "maximum_delivery_hrs_constraint": max_delivery_hrs,
        "profit_per_sales_volume": profit_per_sales
    }
    api_json = json.dumps(api_json)  # Converting dict to json, especially to cater for True/False json types
    _logger.debug(f"[viz_warehouse_allocation] api_json --> {api_json}")

    # Making POST request to API
    _logger.debug(f"[viz_warehouse_allocation] Making API call to {API_URL}")
    api_response = requests.post(API_URL, data=api_json).json()
    _logger.debug(f"[viz_warehouse_allocation] api_response --> {api_response}")

    # Converting results json to dataframes for visualisation
    _logger.debug(f"[viz_warehouse_allocation] Converting JSON responses to pd.DataFrame")
    api_response = dict(api_response)

    warehouses_df = pd.DataFrame(api_response['warehouse_data'])
    townships_df = pd.DataFrame(api_response['township_data'])
    selected_warehouses_df = pd.DataFrame(api_response['warehouse_selection_data'])
    warehouse_township_assignment_df = pd.DataFrame(api_response['warehouse_township_assignment_data'])

    # Visualisation
    _logger.debug(f"[viz_warehouse_allocation] Generating plotly figure")
    fig = viz_warehouse_selection(
        warehouses_df=warehouses_df, townships_df=townships_df,
        selected_warehouses_df=selected_warehouses_df, warehouse_township_assignment_df=warehouse_township_assignment_df
    )
    fig.update_layout(height=800)

    end_time = datetime.now()
    _logger.info(f"[viz_warehouse_allocation] Completed in {end_time - start_time}.")

    return fig

