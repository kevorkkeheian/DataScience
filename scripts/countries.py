import pandas as pd
import world_bank_data as wb


countries = wb.get_countries()
countries = pd.DataFrame(countries).reset_index()


countries["longitude"] = countries["longitude"].astype(str)
countries["latitude"] = countries["latitude"].astype(str)


countries.to_csv("./datasets/world-bank/countries.csv")