import requests
import re
import xmltodict
import pandas as pd
from requests.auth import HTTPBasicAuth
from configs.paths import ODK_SERVER_URL, ODK_USERNAME, ODK_PASSWORD


# Helper function to fetch data from ODK server
def fetch_odk_data(endpoint):
    response = requests.get(endpoint, auth=HTTPBasicAuth(ODK_USERNAME, ODK_PASSWORD))
    if response.status_code == 200:
        return response
    else:
        return response, response.status_code


# Controllers to get the ODK data
def get_users():
    endpoint = f"{ODK_SERVER_URL}/v1/users"
    data = fetch_odk_data(endpoint)
    if data:
        return data.json()
    return data.json()


# Endpoint to get projects
def get_projects():
    endpoint = f"{ODK_SERVER_URL}/v1/projects"
    data = fetch_odk_data(endpoint)
    if data:
        return data.json()
    return data.json()


# Endpoint to get projects details
def get_project_details(project_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}"
    data = fetch_odk_data(endpoint)
    if data:
        return data.json()
    return data.json()


# Endpoint to get project forms
def get_forms_by_project(project_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}/forms"
    data = fetch_odk_data(endpoint)
    if data:
        return data.json()
    return data.json()


# Get form details
def get_form_details(project_id, form_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}/forms/{form_id}"
    data = fetch_odk_data(endpoint)
    if data:
        return data.json()
    return data.json()


# Endpoint to get submissions for a specific form
def get_submissions(project_id, form_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}/forms/{form_id}/submissions"
    data = fetch_odk_data(endpoint)
    if data:
        return list(data.json())
    return list(data.json())


# Get submissions metadata
def get_submission_by_instance_metadata(project_id, form_id, instance_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}/forms/{form_id}/submissions/{instance_id}"
    data = fetch_odk_data(endpoint)
    if data:
        return list(data.json())
    return list(data.json())


# Get Submission answers for a specific form
def get_submission_by_instance(project_id, form_id, instance_id):
    endpoint = f"{ODK_SERVER_URL}/v1/projects/{project_id}/forms/{form_id}/submissions/{instance_id}.xml"
    data = fetch_odk_data(endpoint)
    if data:
        return xmltodict.parse(data.content)
    return list(data.json())
