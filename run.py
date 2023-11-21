import gspread
import google.oauth2.service_account import Credentials

# List of API's requiring access
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# Constant variables
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('habit_tracker')

print('''
╔─────────────────────────────────────────────────────────╗
│██╗  ██╗ █████╗ ██████╗ ██╗████████╗                     │
│██║  ██║██╔══██╗██╔══██╗██║╚══██╔══╝                     │
│███████║███████║██████╔╝██║   ██║                        │
│██╔══██║██╔══██║██╔══██╗██║   ██║                        │
│██║  ██║██║  ██║██████╔╝██║   ██║                        │
│╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝   ╚═╝                        │
│                                                         │
│████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ │
│╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗│
│   ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝│
│   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗│
│   ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║│
│   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝│
╚─────────────────────────────────────────────────────────╝
''')
print("Please press enter to start...")


