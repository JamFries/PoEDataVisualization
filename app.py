import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas
import plotly.express as px

import layouts
import main

df_metamorphCurrency = pandas.read_csv("Data/updatedMetamorph.csv", sep=',', parse_dates=['Date'])
df_deliriumCurrency = pandas.read_csv("Data/updatedDelirium.csv", sep=',', parse_dates=['Date'])
df_harvestCurrency = pandas.read_csv("Data/updatedHarvest.csv", sep=',', parse_dates=['Date'])
df_heistCurrency = pandas.read_csv("Data/updatedHeist.csv", sep=',', parse_dates=['Date'])
df_ritualCurrency = pandas.read_csv("Data/updatedRitual.csv", sep=',', parse_dates=['Date'])

# df_heistItems = pandas.read_csv("Data/updatedHeist_Items.csv", sep=',', parse_dates=['Date'])
# df_ritualItems = pandas.read_csv("Data/updatedRitual_Items.csv", sep=',', parse_dates=['Date'])



df_allLeagueCurrency = pandas.concat([df_ritualCurrency, df_heistCurrency, df_harvestCurrency, df_deliriumCurrency, df_metamorphCurrency])

# df_allLeagueItems = pandas.concat([df_ritualItems, df_heistItems])

# Removes rows so all data is priced in terms of chaos orbs (Ex: 1 alt = 0.3 chaos, not 0.3 chaos = 1 alt)
df_termsOfChaos = df_allLeagueCurrency[df_allLeagueCurrency.Get != "Chaos Orb"]

# df_allLeagueItems = pandas.concat([df_allLeagueItems, df_allLeagueCurrency]) # put everything into one dataset
# print('concatenated all data together to one dataset')
#
# for index, row_series in df_allLeagueItems.iterrows():
#     if (pandas.notna(row_series['Name'])): # Check if the row is an item
#         df_allLeagueItems.at[index, 'Get'] = row_series['Name'] # Set 'Get' value equal to the item's name
#         # This standardizes the data so we only need to access the Get column
# print('set items Get column equal to Name column')



########################################################################################################################
app = dash.Dash()

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), # represents the URL bar, doesnt render anything
    html.Div(id='page-content'), # content will be rendered in this element
])

index_page = layouts.index_page()

currencyLayout = layouts.currencyLayout()
catalystLayout = layouts.catalystLayout()
breachstoneLayout = layouts.breachstoneLayout()
itemLayout = layouts.itemLayout()

@app.callback(
    Output(component_id='page-content', component_property='children'),
    [Input(component_id='url', component_property='pathname')]
)
def display_page(pathname):
    if (pathname == '/currency'):
        return currencyLayout
    elif (pathname == '/catalysts'):
        return catalystLayout
    elif (pathname == '/breachstones'):
        return breachstoneLayout
    elif (pathname == '/items'):
        return itemLayout
    else:
        return index_page



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
    if (len(optionLeague) > 0):
        dfCopy = dfCopy[dfCopy["League"].isin(optionLeague)] # Restrict the dataset to the chosen leagues
    else:
        raise dash.exceptions.PreventUpdate # no leagues were chosen so don't update the graph

    if (len(optionCurrency) > 0):
        df = dfCopy[dfCopy["Get"].isin(optionCurrency)]
        fig = px.line(df, x=df["daysIntoLeague"], y=df["Value"], color=df["League"], line_group=df["Get"], line_dash=df["League"])
    else:
        raise dash.exceptions.PreventUpdate # don't update the graph if all options are removed

    return currencyContainer, leagueContainer, fig

if __name__ == '__main__':
    app.run_server(debug=True)