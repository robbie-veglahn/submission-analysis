# more imports than we need
import geopandas as gpd
import maup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import retrieve_submission_json as subs_json
import retrieve_submission_info as subs_info
import csv
import io

# TO DO:
    # - 1. write this code lol
    # - 2. Ask Nick for way to tell how many submissions of a certain type to..
    #   ...adjust length parameter for API query (lines 31 and 32)


# NOTE: Incomplete file, will use pydantic to join the relevant fields from...
# the submission info with each submissions json for the purposes of using...
# GerryChain partitions while still retaining other info for automation...
# ...(author, datetime, tags, etc.)

# TODO join into a pydantic struct the submission JSON with info dataframe
def joinSubmissions(endpt_url, plans_url, cois_url):
    id_arr, json_obj_arr = subs_json.retrieveSubmissionIDsJson(endpt_url)
    submissions_df = subs_info.retrieveDrawnSubmissionInfo(plans_url, cois_url)
    return id_arr, json_obj_arr, submissions_df

# TODO will be unit tests
def unit_tests(id_arr, json_obj_arr, submissions_df):
    print(id_arr[0])
    print(json_obj_arr[0])
    submissions_df.head()
    return None

# TODO test code
def testingMain():
    url = "https://qp2072772f.execute-api.us-east-2.amazonaws.com/dev/submissions/districtr-ids"
    # TODO #2 automate length check into the api call
    plans_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=plan&length=500"
    cois_url = "https://o1siz7rw0c.execute-api.us-east-2.amazonaws.com/prod/submissions/csv?type=coi&length=500"
    id_arr, json_obj_arr, submissions_df = joinSubmissions(
                                                      url, plans_url, cois_url)
    unit_tests(id_arr, json_obj_arr, submissions_df)
    return None

# testingMain()