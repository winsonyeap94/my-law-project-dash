# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# Font-Awesome Icons
FONT_AWESOME = "https://use.fontawesome.com/releases/v5.7.2/css/all.css"
 
# bootstrap theme
# https://bootswatch.com/lux/
external_stylesheets = [dbc.themes.LITERA, dbc.themes.BOOTSTRAP, FONT_AWESOME]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.config.suppress_callback_exceptions = True