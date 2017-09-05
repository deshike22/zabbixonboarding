import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
# Provide your Google api access credential file name
credentialfile = 'XXX.json'
credentials = ServiceAccountCredentials.from_json_keyfile_name(credentialfile, scope)
gc = gspread.authorize(credentials)


def spreadsheetdata(spreadsheeturl, sheet):
    spreadsheet = gc.open_by_url(spreadsheeturl)
    worksheet = spreadsheet.worksheet(sheet)
    criteria_re = re.compile(r'(add|update)$')
    values_list = worksheet.findall(criteria_re)
    return worksheet, values_list


def spreadsheetdataall(spreadsheeturl, sheet):
    spreadsheet = gc.open_by_url(spreadsheeturl)
    worksheet = spreadsheet.worksheet(sheet)
    criteria_re = re.compile(r'(add|update|delete)$')
    values_list = worksheet.findall(criteria_re)
    return worksheet, values_list
