import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Constants and Sheets
scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']
# Google Sheet credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('DailyPoll-ae4889da60e5.json', scope)
gc = gspread.authorize(credentials)

responses = gc.open("QOTD Responses").sheet1
data = pd.DataFrame(responses.get_all_records())
vals = data['Response'].value_counts()

print("{} currently has {} votes. \n{} currently has {} votes.".format(vals.index[0],vals[0],vals.index[1],vals[1]))
