import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas
import plotly.express as px

df_heistCurrency = pandas.read_csv("Data/Heist.2020-09-18.2021-01-11.currency.csv", sep=';', parse_dates=['Date'])
df_ritualCurrency = pandas.read_csv("Data/Ritual.2021-01-15.2021-04-12.currency.csv", sep=';', parse_dates=['Date'])
# print(df_ritualCurrency.dtypes)

df_allLeagueCurrency = pandas.concat([df_ritualCurrency, df_heistCurrency])

# Removes rows so all data is priced in terms of chaos orbs (Ex: 1 alt = 0.3 chaos, not 0.3 chaos = 1 alt)
df_termsOfChaos = df_allLeagueCurrency[df_allLeagueCurrency.Get != "Chaos Orb"]
# fig = px.line(df_termsOfChaos, x=df_termsOfChaos["Date"], y=df_termsOfChaos["Value"], color=df_termsOfChaos["Get"],
#               line_group=df_termsOfChaos["Get"], hover_name=df_termsOfChaos["Get"])

# Separate the data into categories to more clearly see things on a graph
# df_catalysts = df_termsOfChaos[df_termsOfChaos['Get'].str.contains("Catalyst")]
# fig = px.line(df_catalysts, x=df_catalysts["Date"], y=df_catalysts["Value"], color=df_catalysts["Get"],
#              line_group=df_catalysts["Get"], hover_name=df_catalysts["Get"])

########################################################################################################################
app = dash.Dash()

app.layout = html.Div([
    html.H1("PoE Data Visualization using Dash", style={'text-align': 'center'}),

    dcc.Dropdown(
        id='league-dropdown',
        options=[
            {'label': 'Ritual SC', 'value': 'Ritual'},
            {'label': 'Heist SC', 'value': 'Heist'},
        ],
        multi=False,
        value='Ritual',
        style={'width': '40%'},
        clearable=False,
    ),
    html.Div(id='league-output-container', children=[]),

    dcc.Dropdown(
        id='currency-dropdown',
        options=[
            # label is what the user sees. value is the value that matches the data in the dataset
            {'label': 'Orb of Alteration', 'value': 'Orb of Alteration'},
            {'label': 'Exalted Orb', 'value': 'Exalted Orb'},
        ],
        multi=False,
        value='Orb of Alteration',
        style={'width': "40%"},
        clearable=False,
    ),

    html.Div(id='currency-output-container', children=[]),
    html.Br(),

    dcc.Graph(id='Graph1', figure={})
])

# Connect the plotly graph with the dash components
@app.callback(
    [Output(component_id='currency-output-container', component_property='children'),
     Output(component_id='league-output-container', component_property='children'),
     Output(component_id='Graph1', component_property='figure')],
    [Input(component_id='currency-dropdown', component_property='value'),
     Input(component_id='league-dropdown', component_property='value')]
)
def update_graph(optionCurrency, optionLeague):
    print(optionCurrency)
    currencyContainer = "The currency chosen by the user was: {}".format(optionCurrency)
    leagueContainer = "The league chosen by the user was: {}".format(optionLeague)

    dfCopy = df_termsOfChaos.copy()
    dfCopy = df_termsOfChaos[df_termsOfChaos["Get"] == optionCurrency] #Set the dataset to be only of the value selected

    dfCopy = dfCopy[dfCopy["League"] == optionLeague] # Restrict the dataset to the chosen league

    fig = px.line(dfCopy, x=dfCopy["Date"], y=dfCopy["Value"])

    return currencyContainer, leagueContainer, fig

if __name__ == '__main__':
    app.run_server(debug=True)