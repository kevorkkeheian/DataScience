# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import pyodbc


ConfirmedCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
RecoveredCases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
Deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

ConfirmedCases_ValueColumns = ConfirmedCases.columns[4:]
RecoveredCases_ValueColumns = RecoveredCases.columns[4:]
Deaths_ValueColumns = Deaths.columns[4:]



ConfirmedCases = pd.melt(ConfirmedCases, id_vars=['Country/Region'], 
                          value_vars = ConfirmedCases_ValueColumns,
                          var_name = "Date",
                         value_name = "ConfirmedCases")

RecoveredCases = pd.melt(RecoveredCases, id_vars=['Country/Region'], 
                          value_vars = RecoveredCases_ValueColumns,
                          var_name = "Date",
                         value_name = "RecoveredCases")

Deaths = pd.melt(Deaths, id_vars = ["Country/Region"],
                 value_vars = Deaths_ValueColumns,
                 var_name = "Date",
                 value_name = "Deaths")



ConfirmedCases["Date"] = pd.to_datetime(ConfirmedCases["Date"])
RecoveredCases["Date"] = pd.to_datetime(RecoveredCases["Date"])
Deaths["Date"] = pd.to_datetime(Deaths["Date"])




ConfirmedCases_ByDate = pd.pivot_table(ConfirmedCases, values='ConfirmedCases', index=["Date"], aggfunc=np.sum).sort_values(by = "Date")
RecoveredCases_ByDate = pd.pivot_table(RecoveredCases, values = "RecoveredCases", index = ["Date"], aggfunc = np.sum).sort_values(by = "Date")
Deaths_ByDate = pd.pivot_table(Deaths, values = "Deaths", index = ["Date"], aggfunc = np.sum).sort_values(by = "Date")



#Creating By Country Pivot Tables
ConfirmedCases_ByCountry = pd.pivot_table(ConfirmedCases, values = "ConfirmedCases", index = ["Country/Region"], aggfunc = np.max)
RecoveredCases_ByCountry = pd.pivot_table(RecoveredCases, values = "RecoveredCases", index = ["Country/Region"], aggfunc = np.max)
Deaths_ByCountry = pd.pivot_table(Deaths, values = "Deaths", index = ["Country/Region"], aggfunc = np.max)




COVID19_ByDate = ConfirmedCases_ByDate.merge(RecoveredCases_ByDate, on = "Date").merge(Deaths_ByDate, on = "Date")
COVID19_ByCountry = ConfirmedCases_ByCountry.merge(RecoveredCases_ByCountry, on = "Country/Region").merge(Deaths_ByCountry, on = "Country/Region")



COVID19_ByDate.to_csv('./datasets/COVID19_ByDate.csv', sep=',')
COVID19_ByCountry.to_csv('./datasets/COVID19_ByCountry.csv',  sep=',')












ConfirmedCases["Type"] = "ConfirmedCases"
RecoveredCases["Type"] = "Recoveries"
Deaths["Type"] = "Deaths"


ConfirmedCases.rename(columns = {"ConfirmedCases" : "Value"}, inplace = True)
RecoveredCases.rename(columns = {"RecoveredCases" : "Value"}, inplace = True)
Deaths.rename(columns = {"Deaths" : "Value"}, inplace = True)


CovidCases = ConfirmedCases.append(RecoveredCases, ignore_index=True).append(Deaths, ignore_index = True)





CovidCases_Pivot = pd.pivot_table(CovidCases, values = "Value", index = ["Country/Region", "Date"], columns = "Type", aggfunc = np.sum)
CovidCases = CovidCases_Pivot.reset_index()
CovidCases.to_csv("./datasets/details/CovidCases.csv")
