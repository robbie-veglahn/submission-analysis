# more imports than we need
import geopandas as gpd
import maup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import retrieve_submission_json as phase_1
import csv
import io

# TO DO:
    # - 1. Ask Nick for way to tell how many submissions of a certain type to..
    #   ...adjust length parameter for API query
    # - 2. Ask Nick for ways to avoid security check on API call (line 26)

# csvRead takes in a url (api endpt to query on given submission portal) to ...
# find in csv form data from the portal, and returns a pandas dataframe     ...
# filled with the portal info
    # url: str -> read_file: DataFrame
def csvRead(url):
    # TODO #2: temp fix for the purposes of user-agent api call barrier
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}  
    r = requests.get(url, headers=headers).content
    read_file = pd.read_csv(io.StringIO(r.decode('utf-8')))
    return read_file

# retrieveSubmissionInfo is a simple wrapper funct, takes in a url (api...
# ...query for submissions in a portal) and returns a pandas dataframe 
# # NOTE: url can be query on plans, cois, written subs, or all plan types
    # url: str -> submission: DataFrame
def retrieveSubmissionInfo(url):
    return csvRead(url)

# retrieveDrawnSubmission is a simple wrapper funct, takes in plans_ulr (api...
# ...query for all plans in a portal) and a cois_url (query for all cois in..
# ...a portal) and returns a pandas dataframe of all plan and coi submissions
    # plans_url: str, cois_url: str -> submission: DataFrame
def retrieveDrawnSubmissionInfo(plans_url, cois_url):
    cois = csvRead(cois_url)
    plans = csvRead(plans_url)
    submissions = plans.append(cois, ignore_index = True)
    return submissions