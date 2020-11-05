import requests
import pandas as pd
import numpy as np
import pyodbc

url = 'https://www.worldometers.info/coronavirus/'
html = requests.get(url).content
CasesByCountry = pd.read_html(html)
CasesByCountry_Now = CasesByCountry[0]
CasesByCountry_Yesterday = CasesByCountry[-1]


CasesByCountry_Now = CasesByCountry_Now.fillna(0)
CasesByCountry_Yesterday = CasesByCountry_Yesterday.fillna(0)

if CasesByCountry_Now['NewCases'].dtypes == object:
    CasesByCountry_Now['NewCases'] = CasesByCountry_Now['NewCases'].str.replace(',', '')

if CasesByCountry_Now["NewDeaths"].dtypes == object:
        CasesByCountry_Now['NewDeaths'] = CasesByCountry_Now['NewDeaths'].str.replace(',', '')


if CasesByCountry_Yesterday['NewCases'].dtypes == object:
    CasesByCountry_Yesterday['NewCases'] = CasesByCountry_Yesterday['NewCases'].str.replace(',', '')

if CasesByCountry_Yesterday['NewDeaths'].dtypes == object:
    CasesByCountry_Yesterday['NewDeaths'] = CasesByCountry_Yesterday['NewDeaths'].str.replace(',', '')



CasesByCountry_Now["NewCases"] = CasesByCountry_Now["NewCases"].astype(float)
CasesByCountry_Now["NewDeaths"] = CasesByCountry_Now["NewDeaths"].astype(float)

CasesByCountry_Yesterday["NewCases"] = CasesByCountry_Yesterday["NewCases"].astype(float)
CasesByCountry_Yesterday["NewDeaths"] = CasesByCountry_Yesterday["NewDeaths"].astype(float)


CasesByCountry_Now = CasesByCountry_Now.fillna(0)
CasesByCountry_Yesterday = CasesByCountry_Yesterday.fillna(0)




CasesByCountry_Now.to_csv('./datasets/worldmeter_now.csv', sep = ",")
CasesByCountry_Yesterday.to_csv('./datasets/worldmeter_yesterday.csv', sep = ",")








