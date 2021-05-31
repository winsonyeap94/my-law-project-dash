import dash
from dash.dependencies import Input, Output, State

from app import app
from src.data_loading import *
from src.classes import *


# ====================================================================================================
# Plotting selected chart
# ====================================================================================================
@app.callback(
    [Output('home_h2_selected_stock', 'children'), Output('home_viz_bollingerbands', 'figure'),
     Output('home_div_ticker_symbol', 'children'), Output('home_div_ticker_name', 'children'),
     Output('home_div_last_closing_price', 'children'), 
     Output('home_div_recommendation', 'children'), Output('home_div_recommendation_subtext', 'children'),
     Output('home_div_ticker_description', 'children'), 
     Output('home_div_buy_range', 'children'), 
     Output('home_div_take_profit', 'children'), Output('home_div_take_profit_subtext', 'children'),
     Output('home_div_stop_loss', 'children'), Output('home_div_stop_loss_subtext', 'children'),
     Output('home_div_risk_to_reward', 'children')],
    [Input('home_dropdown_symbol', 'selectedValue')]
)
def plot_bband_chart(selected_symbol):

    # Getting selecting symbol
    selected_stock = Stock(ticker_symbol=selected_symbol)
    ticker_name = selected_stock.ticker_name

    # Plotting chart
    bband_fig = selected_stock.plot_bbands(show=False)
    bband_fig.update_layout(height=700)

    # Getting stock info & statistics
    last_closing_price = f"${selected_stock.get_last_closing_price():.2f}"
    recommendation, recommendation_subtext = selected_stock.get_recommendation()
    ticker_description = selected_stock.get_stock_info()

    # TODO: Integrate with Stock Statistics
    buy_range = '$102 - $109'
    take_profit = '$136.53'
    take_profit_subtext = '18.72% profit'
    stop_loss = '$107.81'
    stop_loss_subtext = '6 loss' 
    risk_to_reward = '1 / 3'
    
    return [
        ticker_name, bband_fig, selected_symbol, ticker_name, 
        last_closing_price, recommendation, recommendation_subtext, ticker_description,
        buy_range, take_profit, take_profit_subtext, stop_loss, stop_loss_subtext, risk_to_reward
    ]



