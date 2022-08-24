# Copyright 2022 Thinh Vu @ GitHub
# See LICENSE for details.

import pandas as pd
import requests
from pandas import json_normalize
import json
import time
import inspect #to show docstring

# from datetime import datetime
# from datetime import timedelta
# import yaml


# DATA EXPORT

def fs_user_export(user_id, report_type, token_key): #userEvents, userPages
    """
    Export events or pages of historical data of a specific user by the userId. Reference [here](https://developer.fullstory.com/get-data-export)
    Args:
        user_id (:obj:`str`, required): the specific userId, usually it should be the email address
        report_type (:obj:`str`, required): "userEvents" or "userPages"
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = 'https://export.fullstory.com/api/v1/export/{}?uid={}'.format(report_type, user_id)
    payload = {}
    headers = {'Authorization' : 'Basic {}'.format(token_key)}
    response = requests.request("GET", url, headers=headers, data=payload)
    if report_type == 'userEvents':
        result = json_normalize(response.json())
    elif report_type == 'userPages':
        result = response
    return result

# USERS
def fs_GetUser(user_id, token_key):
    """
    Get a summary of user information in a DataFrame format. Reference [here](https://developer.fullstory.com/get-user)
    Args:
        user_id (:obj:`str`, required): the specific userId, usually it should be the email address
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = 'https://api.fullstory.com/users/v1/individual/{}'.format(user_id)
    payload = {}
    headers = {'Authorization' : 'Basic {}'.format(token_key)}
    response = requests.request("GET", url, headers=headers, data=payload)
    result = json_normalize(response.json())
    return result



# SEGMENTS

def fs_list_segment(token_key): 
    """
    Get a list of all available segments on your Fullstory account. Reference [here](https://developer.fullstory.com/list-segments)
    Args:
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = 'https://api.fullstory.com/segments/v1'
    payload = {}
    headers = {'Authorization' : 'Basic {}'.format(token_key)}
    response = requests.request("GET", url, headers=headers, data=payload).json()
    result = json_normalize(response['segments'])
    return result

def fs_segment_export(segment_id, report_type, start_date, end_date, token_key):
    """
    Return the segment export as a DataFrame.
    Args:
        segment_id (:obj:`str`, required): The ID of a specific segment on Fullstory. It should look like this "ofHlcGlbWdwX"
        report_type (:obj:`str`, required): Can be "TYPE_EVENT" or "TYPE_INDIVIDUAL"
        start_date (:obj:`str`, required): use this datetime format "2022-01-01T00:00:00Z"
        start_date (:obj:`str`, required): use this datetime format "2022-08-22T23:59:59Z"
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    operationId = fs_schedule_segment_export(segment_id, report_type, "FORMAT_CSV", start_date, end_date, token_key)['operationId']
    time.sleep(3)
    searchExportId = fs_operation_status(operationId, token_key)['results']['searchExportId']
    export_url = fs_export_result(searchExportId, token_key)['location']
    df = pd.read_csv(export_url, compression='gzip')
    return df

## Create Segment Export

def fs_schedule_segment_export(segment_id, report_type, report_format, start_date, end_date, token_key):
    """
    Schedules an export based on the provided segment and returns the operationId. Reference [here](https://developer.fullstory.com/create-segment-export)
    The progress and results of the export can be fetched from the operations API
    Args:
        segment_id (:obj:`str`, required): The ID of a specific segment on Fullstory. It should look like this "ofHlcGlbWdwX"
        report_type (:obj:`str`, required): Can be "TYPE_EVENT" or "TYPE_INDIVIDUAL"
        report_format(:obj:`str`, required): Required. Determines the data format of the export. Options are "FORMAT_JSON", "FORMAT_CSV", and "FORMAT_NDJSON". Suggested to use "FORMAT_CSV" in this python client.
        start_date (:obj:`str`, required): use this datetime format "2022-01-01T00:00:00Z"
        start_date (:obj:`str`, required): use this datetime format "2022-08-22T23:59:59Z"
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = "https://api.fullstory.com/segments/v1/exports"
    payload = json.dumps({
        "segmentId": "{}".format(segment_id),
        "type": "{}".format(report_type),
        "format": "{}".format(report_format),
        "timeRange": {
            "start": "{}".format(start_date),
            "end": "{}".format(end_date)
        }
    })
    headers = {
        'Authorization': 'Basic {}'.format(token_key),
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

## Operation status

def fs_operation_status(operationId, token_key):
    """
    Get details about a specific operation. Return a "searchExportId" which can be used to retrieve the export result. Reference [here](https://developer.fullstory.com/get-operation)
    Args:
        operationId (:obj:`str`, required): The ID of a specific operation on Fullstory. It can be retrieved from the segment_export function.
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = "https://api.fullstory.com/operations/v1/{}".format(operationId)
    payload = ""
    headers = {
        'Authorization': 'Basic {}'.format(token_key),
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

## Get Export result
def fs_export_result(searchExportId, token_key):
    """
    Gets the results for a scheduled export. Return a link that can be used to retrieve the exported CSV gzip file. Reference [here](https://developer.fullstory.com/get-export-results)
    Args:
        searchExportId (:obj:`str`, required): The ID of a specific operation on Fullstory. It can be retrieved from the segment_export function.
        token_key (:obj:`str`, required): Fullstory API key (can be an API key from any roles)
    """
    url = "https://api.fullstory.com/search/v1/exports/{}/results".format(searchExportId)
    payload = ""
    headers = {
    'Authorization': 'Basic {}'.format(token_key),
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()

# DOCSTRING HELPER
def fs_help(function_name):
    """
    Show any function's docstring. Ex: help_doc('fs_export_result').
    Args:
        function_name (:obj:`str`, required): Name of the target function
    """
    print(inspect.getdoc(function_name))