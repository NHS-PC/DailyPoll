import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime
import numpy as np
import connexion

scope = ['https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive']
    # Google Sheet credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name('DailyPoll-ae4889da60e5.json', scope)
gc = gspread.authorize(credentials)

def get_counts():
    responses = gc.open("QOTD Responses").sheet1
    data = pd.DataFrame(responses.get_all_records())
    vals = data['Response'].value_counts()
    return(vals)

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read():
    RESULTS = {
        "First": {
            "name": get_counts().index.tolist()[0],
            "count": str(get_counts()[0]),
            "timestamp": get_timestamp(),
        },
        "Second": {
            "name": get_counts().index.tolist()[1],
            "count": str(get_counts()[1]),
            "timestamp": get_timestamp()
        }
    }
    # Create the list of results from our data
    return [RESULTS[key] for key in RESULTS.keys()]