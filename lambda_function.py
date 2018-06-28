from googleSheet import GoogleSheet
import datetime
import os

## Can set these up as encrypted variables in AWS lambda console and grab using os ##
#TWILIO_SMS_URL = "https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

"""
So the assumption is that you are using Twilio as call attribution -- phone number on the
listing (which is a Twilio Number) is dialed by user (the number you are logging in the Google Sheet as
 'Arrived From'), then that call is fwded to the actual contractor's number
  (The number you want to log in the google sheet as 'Sent To' on this event)
  
  Tying it all together: 
  Twilio Number Dialed/click to called by consumer 
  -> Twilio Number directs on call to AWS API Gateway w/ Parameters
  -> API Gateway invokes Lambda Function passing event data (parameters from Twilio) from call 
  -> Our Lambda function runs logging info in the Google Sheet (and quite frankly whatever else we want to do)
  -> Call is made to the contractor number that is associated/tied to what we want
  using <Dial></Dial> Twilio XML
"""

# Number we want to eventually use Twilio's XML to Dial to #
#contractorNumber = '+'

def lambda_handler(event, context, contractorNumber):

    # the event payload from the initial twilio call fed by our API gateway in JSON dictionary #
    to_number = event['To']   ## Our Twilio number we intercepted
    from_number = event['From']  ## The consumer number that we want to put in google sheet

    ## Fire the Google Sheet log solution here ##
    # You could have the timestamp function - 'datetime.datetime.now()' run at the very
    # beginng to maybe get a little more accurate representation of when the call was was made from the site
    GoogleSheet.sheet_update(gs='yourChoice', timestamp=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             phone_arrived=from_number, phone_sent=contractorNumber)

    openXml = '<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Dial>'
    closeXml = '</Dial></Response>'
    return openXml+contractorNumber+closeXml
