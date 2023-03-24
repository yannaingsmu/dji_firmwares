import requests
import pandas as pd

def download(url,dest):
    #url = 'https://dl.djicdn.com/downloads/inspire_1/WM610_FW_V01.07.00.90.zip'
    r = requests.get(url, allow_redirects=True)

    open('./downloads/'+dest, 'wb').write(r.content)



data = pd.read_csv('./dji_firmware_collection.csv')
link = data.download_link.tolist()
name = data.download_name.tolist()

for x,y in zip(link,name):
   
    if not str(x) == 'nan':
        print(x , " ***** ", type(x))
        download(x,y)
        print(str(y)+" done.")
