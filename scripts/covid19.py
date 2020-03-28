import requests
import pandas as pd
import numpy as np
import pyodbc

url = 'https://www.worldometers.info/coronavirus/'
html = requests.get(url).content
CasesByCountry = pd.read_html(html)
CasesByCountry_Now = CasesByCountry[0]
CasesByCountry_Yesterday = CasesByCountry[-1]

CasesByCountry_Now.to_csv('./datasets/worldmeter_now.csv', sep = ",")
CasesByCountry_Yesterday.to_csv('./datasets/worldmeter_yesterday.csv', sep = ",")




CasesByCountry_Now = CasesByCountry_Now.fillna(0)