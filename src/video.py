import os
from googleapiclient.discovery import build


class Video:

    API_KEY: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, video_id: str):
        self.__video_id = video_id
        if self.__video_verify_id(video_id) != 0:

            self.__video_response = self.__youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                                 id=self.video_id).execute()
            self.__video_title = self.__video_response['items'][0]['snippet']['title']
            self.__video_url = f"https://www.youtube.com/watch?v={self.video_id}"
            self.__view_count = self.__video_response['items'][0]['statistics']['viewCount']
            self.__like_count = self.__video_response['items'][0]['statistics']['viewCount']
        else:
            self.__title = None
            self.__video_url = None
            self.__view_count = None
            self.__like_count = None

    def __str__(self) -> str:
        return self.video_title

    def __video_verify_id(self, video_id):
        video_response = self.__youtube.videos().list(part='status', id=video_id).execute()
        search_count = video_response['pageInfo']['totalResults']
        return search_count

    @property
    def video_id(self) -> str:
        return self.__video_id

    @property
    def video_title(self) -> str:
        return self.__video_title

    @property
    def video_url(self) -> str:
        return self.__video_url

    @property
    def view_count(self) -> str:
        return self.__view_count

    @property
    def like_count(self) -> str:
        return self.__like_count
