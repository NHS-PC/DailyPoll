import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

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

RESULTS = {
    "First": {
    "name": get_counts().index.tolist()[0],
    "count": get_counts()[0],
    "timestamp": get_timestamp(),
    },
    "Second": {
        "name": get_counts().index.tolist()[1],
        "count": get_counts()[1],
        "timestamp": get_timestamp()
    }
}

def read():
    """
    This function responds to a request for /api/results
    with the complete lists of results

    :return:        sorted list of results
    """
    # Create the list of results from our data
    return [RESULTS[key] for key in sorted(RESULTS.keys())]

print(read())
