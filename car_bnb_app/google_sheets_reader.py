from googleapiclient.discovery import build
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'carbnb-keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of spreadsheet.
SAMPLE_SPREADSHEET_ID = '1feSrEyzzBgmhfa3GAcCFivTtbmlvy0JUMQFw2QmtZEs'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API - Person
sheet = service.spreadsheets()
person = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="person!A1:E8").execute()
values = person.get('values', [])
print(values)

# Call (read) the Sheets API - Car
sheet = service.spreadsheets()
car = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                         range="car!A1:F11").execute()
values = car.get('values', [])
print(values)

# Call the Sheets API - Rent
sheet = service.spreadsheets()
rent = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range="rent!A1:E4").execute()
values = rent.get('values', [])
print(values)

# Write (update) to Sheets API - Car
test_values = [[8, "John", "Doe", 91, "Lalaland"], [9, "Jane", "Doe", 87, "Lalaland"],
               [10, "Crazy", "Guy", 19, "Lalaland"]]

request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="person!A9", valueInputOption="USER_ENTERED", body={"values": test_values}).execute()

print(request)