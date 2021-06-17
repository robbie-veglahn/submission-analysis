# more imports than we need
import geopandas as gpd
import maup
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# planRead takes in a plan_id string, makes an api call passing in the...
# plan_id into the planRead districtr function, and returns the data...
# associated with the plan_id in JSON format
    # plan_id: int -> data: json obj
def planRead(plan_id):
    url = "https://districtr.org/.netlify/functions/planRead?id=%s" % plan_id
    r = requests.get(url)
    data = json.loads(r.text)
    return data

# retrieveSubmissionJson takes a url (an endpoint to a given state's...
# ...submission portal), returns id_arr and json_obj_arr:
# ******** id_arr: array of info for all submissions in the form...
# [(plan_id, plan_type, plan_link),...], where plan_type is either COI or   ...
#  districting plan
#  ******** json_obj_arr: an array of JSON objects, each corresponding to one..
# of the portal submissions
    # url: str -> id_arr: [(int, str, str)], json_obj_arr: [json obj] 
def retrieveSubmissionIDsJson(url):
    r = requests.get(url)
    subs_json = json.loads(r.text)
    num_rows = int(subs_json['rowCount'])
    id_arr = [(None, None)] * num_rows
    json_obj_arr = [None] * num_rows
    for i in range(0, num_rows):
        # Phase 1, read in the ids and fill id_arr w id, link, and plan type
        plan_link = subs_json['rows'][i]['link']
        plan_id = plan_link[-5:]
        plan_type = subs_json['rows'][i]['type']
        id_arr[i] = (plan_id, plan_type, plan_link)
        # Phase 2, use the ids to retrieve plan's JSON obj to fill json_obj_arr
        json_obj_arr[i] = planRead(plan_id)
    return id_arr, json_obj_arr


    