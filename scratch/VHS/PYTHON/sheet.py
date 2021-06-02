import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('MyFirst-da0e8937a07b.json', scope)
client = gspread.authorize(creds)

sheet = client.open('n26-csv-transactions').sheet1
pp = pprint.PrettyPrinter()
df = sheet.get_all_records()
pp.pprint(df)
