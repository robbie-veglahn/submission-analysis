# more imports than we need
import geopandas as gpd
import maup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
import csv
import io
import pydantic
from pydantic import BaseModel
from typing import Tuple

class Submission(pydantic.BaseModel):
    """
    pydantic class containing districtr link, districtr plan (assignment),  ...
    the type of the plan 
    """
    link: str
    districtr_plan: dict # dict: districtr json obj
    plan_type: str
    id: str

def submissions(endpt_url: str, plans_url: str, cois_url: str,
                wr_url: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Takes in endpoint for all districtr ids in a portal 
    """
    submissions = retrieveSubmissionIDsJson(endpt_url)
    submissions.sort(key=lambda x: x.id)
    plan_submissions = [sub for sub in submissions if sub.plan_type == "plan"]
    coi_submissions = [sub for sub in submissions if sub.plan_type == "coi"]
    plan_submissions_df = csvRead(plans_url)
    coi_submissions_df = csvRead(cois_url)
    written_submissions_df = csvRead(wr_url)
    assert len(plan_submissions) == len(plan_submissions_df)
    assert len(coi_submissions) == len(coi_submissions_df)
    plan_submissions_df['plan_id'] = plan_submissions_df["link"].map(
                                                        lambda link: link[-5:])
    plan_submissions_df = plan_submissions_df.sort_values(
                                                by=['plan_id'], ascending=True)
    coi_submissions_df['plan_id'] = coi_submissions_df["link"].map(
                                                        lambda link: link[-5:])
    coi_submissions_df = coi_submissions_df.sort_values(
                                                by=['plan_id'], ascending=True)
    plan_submissions_df['districtr_data'] = plan_submissions
    coi_submissions_df['districtr_data'] = coi_submissions
    return plan_submissions_df, coi_submissions_df, written_submissions_df

def planRead(plan_id: int) -> dict: #(dict: json obj)#
    """
    takes in plan_id string, makes api call w/ plan_id to the planRead funct...
    in netlify, and returns the data associated with the plan_id in JSON format
    """
    url = "https://districtr.org/.netlify/functions/planRead?id=%s" % plan_id
    r = requests.get(url)
    data = json.loads(r.text)
    return data

def retrieveSubmissionIDsJson(url: str) -> list: #list: list[Submission]
    """
    retrieveSubmissionJson takes a url (an endpoint to a given state's...
    submission portal), returns a list of filled Submission objects
    """
    r = requests.get(url)
    subs_json = json.loads(r.text)
    num_rows = int(subs_json['rowCount'])
    submissions = []
    for i in range(0, num_rows):
        # Phase 1, retrieve link, id, type of plan
        plan_link = subs_json['rows'][i]['link']
        plan_id = plan_link[-5:]
        plan_type = subs_json['rows'][i]['type']
        # Phase 2, fill submission with phase 1 + the ditrictr plan (assignment)
        submissions.append(
                Submission(link=plan_link, plan_type=plan_type,
                           id=plan_id, districtr_plan=planRead(plan_id)))
    return submissions

def csvRead(url: str) -> pd.DataFrame:
    """
    takes in a url (api endpt to query on given submission portal) to find  ...
    in csv form data from the portal, and returns a pandas dataframe filled ...
    with the portal info
    """
    # TODO #2: temp fix for the purposes of user-agent api call barrier
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}  
    r = requests.get(url, headers=headers).content
    read_file = pd.read_csv(io.StringIO(r.decode('utf-8')))
    return read_file
