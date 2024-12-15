
     
import requests
url = "http://127.0.0.1:8000/inscription/"

data = {
    "nom_complet":"promesse",
    "email": "oscara@gmail.com",
    "telephone":"12154554554545",
    "adresse":"sdfodfif",
    
}
response = requests.post(url, json=data)
try  :
    if response.status_code == 201:
        print("ok")
except Exception as e:
    print(e)