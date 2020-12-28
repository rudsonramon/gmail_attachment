from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from message_details import get_message
from datetime import datetime, timedelta
import time

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    try:
        """Shows basic usage of the Gmail API.
        Lists the user's Gmail labels.
        """
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('gmail', 'v1', credentials=creds)

        nextPageToken = ''
        scheduled_time = datetime.now() - timedelta(hours=2)
        query = 'after:' + str(scheduled_time)
        print('AFTER: ', scheduled_time)
        while nextPageToken != None:
            if nextPageToken != '':
                print(
                    'IF CONDITION - (if nextPageToken != '') :: -=====>>>>>>>>>>>>> ', nextPageToken)
                results = service.users().messages().list(
                    userId='me', q=query, pageToken=nextPageToken).execute()
            else:
                print('ELSE CONDITION:: -=====>>>>>>>>>>>>> ', nextPageToken)
                results = service.users().messages().list(
                    userId='me', q=query).execute()
            messages = results.get('messages', [])
            nextPageToken = results.get('nextPageToken')

            if not messages:
                print('No messages found.')
            else:
                print('Em processamento...')
                for message in messages:
                    for message in messages:
                        get_message(service, message_id=message['id'])
                    break
    except Exception as e:
        print(e)


if __name__ == '__main__':
    while True:  # Infinite loop
        main()
        time.sleep(120)  # Wait 600s (10 min) before re-entering the cycle
