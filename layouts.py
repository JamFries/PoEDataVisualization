import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

def index_page():
    return html.Div([
        html.H1("PoE Data Visualization using Dash", style={'text-align': 'center', 'background-color': 'lightblue'}),

        dcc.Link('Navigate to "/currency"', href='/currency'),
        html.Br(),
        dcc.Link('Navigate to "/catalysts"', href='/catalysts'),
        html.Br(),
        dcc.Link('Navigate to "/breachstones"', href='/breachstones'),
    ])

def currencyLayout():
    return html.Div([
        html.H1("PoE Data Visualization using Dash", style={'text-align': 'center', 'background-color': 'lightblue'}),

        dcc.Dropdown(
            id='league-dropdown',
            options=[
                {'label': 'Ritual SC', 'value': 'Ritual'},
                {'label': 'Heist SC', 'value': 'Heist'},
            ],
            multi=True,
            value=['Ritual'],
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
                {'label': 'Orb of Fusing', 'value': 'Orb of Fusing'},
                {'label': 'Divine Orb', 'value': 'Divine Orb'},
                {'label': 'Blessed Orb', 'value': 'Blessed Orb'},
                {'label': "Armourer's Scrap", 'value': "Armourer's Scrap"},
                {'label': "Blacksmith's Whetstone", 'value': "Blacksmith's Whetstone"},
                {'label': "Orb of Transmutation", 'value': "Orb of Transmutation"},
                {'label': "Orb of Augmentation", 'value': "Orb of Augmentation"},
                {'label': "Jeweller's Orb", 'value': "Jeweller's Orb"},
                {'label': "Portal Scroll", 'value': "Portal Scroll"},
                {'label': "Chromatic Orb", 'value': "Chromatic Orb"},
                {'label': "Orb of Alchemy", 'value': "Orb of Alchemy"},
                {'label': "Silver Coin", 'value': "Silver Coin"},
                {'label': "Glassblower's Bauble", 'value': "Glassblower's Bauble"},
                {'label': "Orb of Regret", 'value': "Orb of Regret"},
                {'label': "Orb of Chance", 'value': "Orb of Chance"},
                {'label': "Orb of Scouring", 'value': "Orb of Scouring"},
                {'label': "Regal Orb", 'value': "Regal Orb"},
                {'label': "Gemcutter's Prism", 'value': "Gemcutter's Prism"},
                {'label': "Perandus Coin", 'value': "Perandus Coin"},
                {'label': "Scroll of Wisdom", 'value': "Scroll of Wisdom"},
                {'label': "Vaal Orb", 'value': "Vaal Orb"},
                {'label': "Rogue's Marker", 'value': "Rogue's Marker"},
                {'label': "Cartographer's Chisel", 'value': "Cartographer's Chisel"},
                {'label': "Orb of Annulment", 'value': "Orb of Annulment"},
                {'label': "Stacked Deck", 'value': "Stacked Deck"},
                {'label': "Ancient Orb", 'value': "Ancient Orb"},
                {'label': "Orb of Horizons", 'value': "Orb of Horizons"},
                {'label': "Orb of Binding", 'value': "Orb of Binding"},
                {'label': "Engineer's Orb", 'value': "Engineer's Orb"},
            ],
            multi=True,
            value=['Orb of Alteration'],
            style={'width': "40%"},
        ),

        html.Div(id='currency-output-container', children=[]),
        html.Br(),

        dcc.Graph(id='Graph1', figure={})
    ])

def catalystLayout():
    return html.Div([
        html.H1("PoE Data Visualization using Dash", style={'text-align': 'center', 'background-color': 'lightblue'}),

        dcc.Dropdown(
            id='league-dropdown',
            options=[
                {'label': 'Ritual SC', 'value': 'Ritual'},
                {'label': 'Heist SC', 'value': 'Heist'},
            ],
            multi=True,
            value=['Ritual'],
            style={'width': '40%'},
            clearable=False,
        ),
        html.Div(id='league-output-container', children=[]),

        dcc.Dropdown(
            id='currency-dropdown',
            options=[
                # label is what the user sees. value is the value that matches the data in the dataset
                {'label': 'Fertile Catalyst', 'value': 'Fertile Catalyst'},
                {'label': 'Intrinsic Catalyst', 'value': 'Intrinsic Catalyst'},
                {'label': 'Abrasive Catalyst', 'value': 'Abrasive Catalyst'},
                {'label': 'Tempering Catalyst', 'value': 'Tempering Catalyst'},
                {'label': 'Turbulent Catalyst', 'value': 'Turbulent Catalyst'},
                {'label': 'Prismatic Catalyst', 'value': 'Prismatic Catalyst'},
                {'label': 'Imbued Catalyst', 'value': 'Imbued Catalyst'},
            ],
            multi=True,
            value=['Fertile Catalyst'],
            style={'width': "40%"},
        ),

        html.Div(id='currency-output-container', children=[]),
        html.Br(),

        dcc.Graph(id='Graph1', figure={})
    ])

def breachstoneLayout():
    return html.Div([
        html.H1("PoE Data Visualization using Dash", style={'text-align': 'center', 'background-color': 'lightblue'}),

        dcc.Dropdown(
            id='league-dropdown',
            options=[
                {'label': 'Ritual SC', 'value': 'Ritual'},
                {'label': 'Heist SC', 'value': 'Heist'},
            ],
            multi=True,
            value=['Ritual'],
            style={'width': '40%'},
            clearable=False,
        ),
        html.Div(id='league-output-container', children=[]),

        dcc.Dropdown(
            id='currency-dropdown',
            options=[
                # label is what the user sees. value is the value that matches the data in the dataset
                {'label': "Esh's Breachstone", 'value': "Esh's Breachstone"},
                {'label': "Esh's Charged Breachstone", 'value': "Esh's Charged Breachstone"},
                {'label': "Esh's Enriched Breachstone", 'value': "Esh's Enriched Breachstone"},
                {'label': "Esh's Pure Breachstone", 'value': "Esh's Pure Breachstone"},
                {'label': "Tul's Breachstone", 'value': "Tul's Breachstone"},
                {'label': "Tul's Charged Breachstone", 'value': "Tul's Charged Breachstone"},
                {'label': "Tul's Enriched Breachstone", 'value': "Tul's Enriched Breachstone"},
                {'label': "Tul's Pure Breachstone", 'value': "Tul's Pure Breachstone"},
                {'label': "Xoph's Breachstone", 'value': "Xoph's Breachstone"},
                {'label': "Xoph's Charged Breachstone", 'value': "Xoph's Charged Breachstone"},
                {'label': "Xoph's Enriched Breachstone", 'value': "Xoph's Enriched Breachstone"},
                {'label': "Xoph's Pure Breachstone", 'value': "Xoph's Pure Breachstone"},
                {'label': "Uul-Netol's Breachstone", 'value': "Uul-Netol's Breachstone"},
                {'label': "Uul-Netol's Charged Breachstone", 'value': "Uul-Netol's Charged Breachstone"},
                {'label': "Uul-Netol's Enriched Breachstone", 'value': "Uul-Netol's Enriched Breachstone"},
                {'label': "Uul-Netol's Pure Breachstone", 'value': "Uul-Netol's Pure Breachstone"},
                {'label': "Chayula's Breachstone", 'value': "Chayula's Breachstone"},
                {'label': "Chayula's Charged Breachstone", 'value': "Chayula's Charged Breachstone"},
                {'label': "Chayula's Enriched Breachstone", 'value': "Chayula's Enriched Breachstone"},
                {'label': "Chayula's Pure Breachstone", 'value': "Chayula's Pure Breachstone"},
            ],
            multi=True,
            value=["Chayula's Breachstone"],
            style={'width': "40%"},
        ),

        html.Div(id='currency-output-container', children=[]),
        html.Br(),

        dcc.Graph(id='Graph1', figure={})
    ])