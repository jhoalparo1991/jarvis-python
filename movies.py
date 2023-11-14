from decouple import config
import requests
import subprocess as sp

TMDB_API_KEY=config("TMDB_API_KEY")
URL_API=config("URL_API")
TOKEN=config("TOKEN")


def get_movies():
    
    try:
        url = f"{URL_API}&api_key={TMDB_API_KEY}"
        print(url)
        headers = {
            'accept':'application/json',
            'Authorization': f'Bearer {TOKEN}'
        }
        
        # print(headers)
    
        response = requests.get(url,headers)

        data = response.json()['results']
        
        print(data)
        
       
    except Exception as ex:
        print(ex)


get_movies()