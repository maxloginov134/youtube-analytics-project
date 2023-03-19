from googleapiclient.discovery import build
import os
import json


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.url = f"https://www.youtube.com/channel/{channel_id}"
        self.description = self.channel['items'][0]['snippet']['description']
        self.subscribers_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute())

    def to_json(self, filename: str):

        json_object = {
          "id": self.channel_id,
          "title": self.title,
          "video_count": self.video_count,
          "url": self.url,
          "subscribers_count": self.subscribers_count,
          "view_count": self.view_count
        }

        with open(filename, "w") as file:
            json.dump(json_object, file, indent=4)

    @classmethod
    def get_service(cls):
        return cls.youtube

