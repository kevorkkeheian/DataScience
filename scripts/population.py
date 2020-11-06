import pandas as pd
import world_bank_data as wb

population = wb.get_series('SP.POP.TOTL', id_or_value='id', simplify_index=True).reset_index()


population = population.loc[(population['SP.POP.TOTL'] > 0)]
population['SP.POP.TOTL'].fillna(0, inplace=True)


population["SP.POP.TOTL"] = population["SP.POP.TOTL"].astype(int)
population["Year"] = population["Year"].astype(int)
population = population.loc[(population['SP.POP.TOTL'] > 0)]

population.to_csv("./datasets/world-bank/population.csv")