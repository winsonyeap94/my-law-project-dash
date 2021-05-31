import dash
from dash.dependencies import Input, Output, State

from app import app


# ====================================================================================================
# Warehouse Allocation Map
# ====================================================================================================
@app.callback(
    Output('debug-msg', 'children'),
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

    debug_msg = f"optimisation_scenario: {optimisation_scenario} | "
    debug_msg += f"add_delivery_hrs: {add_delivery_hrs} | "
    debug_msg += f"max_delivery_hrs: {max_delivery_hrs} | "
    debug_msg += f"add_despatch_hiring_cost: {add_despatch_hiring_cost} | "
    debug_msg += f"despatch_hiring_cost: {despatch_hiring_cost} | "
    debug_msg += f"add_cost_of_delivery: {add_cost_of_delivery} | "
    debug_msg += f"cost_of_delivery: {cost_of_delivery} | "
    debug_msg += f"delivery_speed: {delivery_speed} | "
    debug_msg += f"despatch_volume_limit: {despatch_volume_limit} | "
    debug_msg += f"working_hours: {working_hours} | "
    debug_msg += f"profit_per_sales: {profit_per_sales} | "

    return debug_msg


