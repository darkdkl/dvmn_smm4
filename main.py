from __future__ import print_function
import pickle
import os
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import re
import time
import telegram


from telegram_posts import send_telegram
from vk_posts import send_vk
from facebook_posts import send_facebook

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


SHEET_ID = os.getenv('SHEET_ID')
RANGE_SHEET = os.getenv('RANGE_SHEET')


def get_id(data):
    id_file = re.findall(r"id=.*;", data)
    return id_file[0][3:-2]


def work_with_the_table():
    creds = None

    data_dir = './data/'
    days = ["понедельник", "вторник", "среда",
            "четверг", "пятница", "суббота", "воскресенье"]
    flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
    creds = flow.run_local_server()


    service = build('sheets', 'v4', credentials=creds)

    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_ID, range=RANGE_SHEET,
                                valueRenderOption='FORMULA').execute()
    table_cells = result.get('values', [])

    gauth = GoogleAuth()

    drive = GoogleDrive(gauth)

    if not table_cells:
        print('No data found.')

    
    for number, row in enumerate(table_cells):

        image = None
        message = None

        if time.localtime()[6] == days.index(row[3]) and time.localtime()[3] == row[4] and 'нет' in row[7]:
            os.makedirs(data_dir, exist_ok=True)

            if row[6]:

                image = drive.CreateFile({'id': get_id((row[6]))})
                
                print(image)
                
                image.GetContentFile(data_dir+image['title'])



                image = f"{data_dir}{image['title']}"

            if row[5]:

                text = drive.CreateFile({'id': get_id((row[5]))})
                message_text_file = data_dir+text['title']+'.txt'

                text.GetContentFile(message_text_file,
                                    mimetype='text/plain')
                with open(message_text_file, 'r') as mesg:
                    message = mesg.read()

            # if row[0] == 'да':

            #     send_vk(message=message, image=image)
            # if row[1] == 'да':
            #     send_telegram(message=message, image=image)
            # if row[2] == 'да':
            #     send_facebook(message=message, image=image)

            cell_number = f'H{number+3}'
            values = [['Да']]
            body = {'values': values}

            result_upd = service.spreadsheets().values().update(spreadsheetId=SHEET_ID,
                                                                range=cell_number, valueInputOption='USER_ENTERED', body=body).execute()
            print(f"{result_upd.get('updatedCells')} cells updated.")


def main():

    while True:
        work_with_the_table()
        time.sleep(300)


if __name__ == '__main__':
    main()
