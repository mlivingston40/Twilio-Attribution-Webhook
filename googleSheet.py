"""
Things you want to log to columns
# Timestamp
# Phone Number where the call arrived from
# Phone Number where the call was sent to
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class GoogleSheet:

    def __init__(self):

        self.scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        ## Could store this in the file bundle source or maybe better suited to encrypt in AWS lambda
        # console as Environment variables then read in w/ os package ##
        self.gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('key.json', self.scope))

    def sheet_update(self, gs, timestamp, phone_arrived, phone_sent):

        ## gs is your google sheet of choice ##

        ## using sheet1 put can parametrize if necessary to do different sheet ##
        opened = self.gc.open(gs).sheet1

        ## append your row of Timestamp, Phone call from, Phone call sent to ##

        # Assuming your google sheet has the columns set up already with
        # Timestamp, Phone Number where the call arrived from, and Phone Number where the call was sent to
        opened.append_row([timestamp, phone_arrived, phone_sent])
