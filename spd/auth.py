import os 
import json 
import spotipy
from pathlib import Path
from spotipy.oauth2 import SpotifyClientCredentials

# For the website and api part 

class SpotifyAutoAuth(object):
    def __init__(self):
        self.parent_path = Path(__file__).resolve(strict=True).parent.parent
        self.__secret_path = os.path.join(self.parent_path, 'secret.json')
    
    def auth(self):
        with open(self.__secret_path, 'r') as api_cred:
            credentials = json.loads(api_cred.read())
        
        spotify_api_object = spotipy.Spotify(
            auth_manager = SpotifyClientCredentials(client_id = credentials['id'], client_secret = credentials['secret'])
        )

        return spotify_api_object


# For library part 

class SpotifyAuthUserLib(object):
    def __init__(self, api_json_credential_path):
        """
        params:
        -------
        api_json_credential_path : json file path that contains the api credentials for spotify
        
        NOTE:
        -----
        The format of the json file must be like this:

        ```
        {
            "id" : "<generated_id>",
            "secret": <generated_secret">
        }
        ```
        """
        self.__secret_path = api_json_credential_path
    
    def auth(self):
        with open(self.__secret_path, 'r') as api_cred:
            credentials = json.loads(api_cred.read())
        
        spotify_api_object = spotipy.Spotify(
            auth_manager = SpotifyClientCredentials(client_id = credentials['id'], client_secret = credentials['secret'])
        )

        return spotify_api_object