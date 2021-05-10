import datetime
import pandas
import matplotlib.pyplot as plt

import plotly.express as px

df_currency = pandas.read_csv("Data/Ritual.2021-01-15.2021-04-12.currency.csv", sep=';', parse_dates=['Date'])
# print(df_currency.dtypes)

# Removes rows so all data is priced in terms of chaos orbs (Ex: 1 alt = 0.3 chaos, not 0.3 chaos = 1 alt)
df_termsOfChaos = df_currency[df_currency.Get != "Chaos Orb"]
fig = px.line(df_termsOfChaos, x=df_termsOfChaos["Date"], y=df_termsOfChaos["Value"], color=df_termsOfChaos["Get"],
              line_group=df_termsOfChaos["Get"], hover_name=df_termsOfChaos["Get"])
fig.show()