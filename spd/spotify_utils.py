import os
import sys 
import json
import spotipy
from pathlib import Path
BASE_PATH = Path(__file__).resolve(strict=True).parent.parent

class SpotifyAPIUtils(object):
    def __init__(self, spotify_api_object):
        """
        params:
        ------
        spotify_api_object : object returned from auth 
        """
        self.spotipy_api = spotify_api_object
    
    def get_raw_results(self, uri_id, type='playlist', limit = 100):
        """
        Just provide the raw resuts
        """
        
        uri = f"spotify:{type}:{uri_id}"

        if type == 'playlist':
            return self.spotipy_api.playlist_items(playlist_id = uri_id, limit = limit)
        
        

    def get_all_the_artist_in_playlist(self):
        pass

    def get_song_details(self):
        """
        Provides the details of a particular song
        """
        pass

    def thumbnail_of_song(self):
        """
        Provides the thumbnail of a particular song
        """
        # Its (images) in the key for the response
        pass 

    def fetch_songs_of_an_artist(self, artist_page_url, request_limit = 100):
        
        pass 

    def get_general_data_of_a_song(self):
        """
        This includes:
        --------------
        1. Song name
        2. Artists
        3. Popularity score
        4. preview song mp3 (optional)
        5. song url
        6. thumbnail
        """
        pass
    
    def get_all_song_info_in_playlist(self, playlist_url, save_into_csv = False):
        pass 

    def create_song_dataset_from_playlist(self, 
                                          playlist_url, 
                                          folder_to_save_path,
                                          donwload_preview_song = False, 
                                          download_full_song = False):
        """
        Creates a csv file containing the columns :
        1. Song name
        2. Artists
        3. Popularity score
        4. song url
        5. thumbnail
        6. preview song mp3 (optional)
        7. Full song mp3 (optional)

        # Here we will just get the csv file containing the song different data and the links
        """
        pass 

    def create_song_dataset_from_particular_artist(self, 
                                                   artist_url, 
                                                   folder_to_save,
                                                   download_preview_song = False, 
                                                   download_full_song = False):
        """
        Same as `create_song_dataset_from_playlist`, but specific to a single artist
        """
        pass 

    def get_artist_biography(self, artist_name):
        pass 

    def get_songs_from_public_playlist(self, playlist_url, response_limit = 100):
        """
        Finds the songs and its corresponding artists and saves to the list
        params:
        ------
        playlist_url : the **public** spotify playlist url
        request_limit : the number of responses per requests
        
        """
        fetched_songs_data = []
        playlist_id = playlist_url.split('/')[-1]
        results = self.spotipy_api.playlist_items(playlist_id=playlist_id, limit = response_limit)

        while True:
            for song_item in results['items']:
                song_name = song_item['track']['name']
                artist_name = song_item['track']['artists'][0]['name']
                fetched_songs_data.append((song_name, artist_name))
            results = self.spotipy_api.next(results)
            if not results:
                print('Parsed all the songs and its corresponding first artists')
                break 
        return fetched_songs_data