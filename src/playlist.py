import datetime
import os
import isodate
from googleapiclient.discovery import build


class PlayList:
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_info = self.youtube.playlists().list(id=playlist_id, part='contentDetails,snippet',
                                                           maxResults=50,).execute()

        self.each_video_info = self.youtube.playlistItems().list(playlistId=self.playlist_id, part='contentDetails',
                                                                 maxResults=50).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.each_video_info['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails, statistics', id=','.join(
            self.video_ids)).execute()

        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/playlist?list={self.playlist_id}'

    @property
    def titles(self):
        return self.title

    @property
    def urls(self):
        return self.url

    @property
    def total_duration(self):
        total_duration = datetime.timedelta()
        video_response = self.video_response

        for video in video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        pop_list = self.video_response
        max_likes = 0
        max_likes_video = None

        for i in range(5):
            like_count = int(pop_list['items'][i]['statistics']['likeCount'])
            if like_count > max_likes:
                max_likes = like_count
                max_likes_video = pop_list['items'][i]['id']
        return f"https://youtu.be/{max_likes_video}"

