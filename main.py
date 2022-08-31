import requests
import pandas
import gui
import creds


gui_w = gui.Fetcher(2)

a = gui_w.x
file_csv = pandas.read_csv("eBird_file.csv")
payload = {}
headers = {
    'X-eBirdApiToken': creds.API

}
parameters = {
    'maxResults': a
}

url = "https://api.ebird.org/v2/data/obs/HR/recent"

response = requests.request("GET", url, headers=headers, data=payload, params=parameters)
response.raise_for_status()
# print(response.status_code)
data_recent = response.json()
for num in range(a):
    data = {
        'comName': [data_recent[num]['comName']],
        'sciName': [data_recent[num]['sciName']],
        'locName': [data_recent[num]['locName']],
        'obsDt': [data_recent[num]['obsDt']],
        # 'howMany': [data_recent[num]['howMany']]
    }
    df = pandas.DataFrame(data)
    df.to_csv("eBird_file.csv", mode='a', index=False, header=False)

print(data_recent)
