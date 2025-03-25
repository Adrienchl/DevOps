import requests

def recuperer_blague():
    url = "https://blague-api.vercel.app/api?mode=global"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        blague = data['blague']
        reponse = data['reponse']
        
        print(f"Blague : {blague}")
        print(f"Réponse : {reponse}")
    else:
        print(f"Erreur {response.status_code}")

recuperer_blague()
