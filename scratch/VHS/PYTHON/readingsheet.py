import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(
         'MyFirst-da0e8937a07b.json', scope) # Your json file here

gc = gspread.authorize(credentials)

wks = gc.open("n26-csv-transactions").sheet1

data = wks.get_all_values()
headers = data.pop(0)

df = pd.DataFrame(data, columns=headers)
print(df.head())
